# Задание 7: RNN для генерации текста
# Код рассчитан на запуск в Google Colab

import tensorflow as tf
import numpy as np
import requests

class TextGenerator:
    def __init__(self, vocab_size, embedding_dim=128, lstm_units=128):
        # TODO: Создать модель c Embedding + LSTM + Dense слоями
        # Архитектура:
        # - Embedding(vocab_size, embedding_dim)
        # - LSTM(lstm_units, return_sequences=True)
        # - LSTM(lstm_units)
        # - Dense(vocab_size, activation='softmax')
        self.model = tf.keras.Sequential([
            tf.keras.layers.Embedding(vocab_size, embedding_dim),
            tf.keras.layers.LSTM(lstm_units, return_sequences=True),
            tf.keras.layers.LSTM(lstm_units),
            tf.keras.layers.Dense(vocab_size, activation='softmax')
        ])
        self.vocab_size = vocab_size

        # словари для кодирования символов (инициализируем позже в preprocess_text)
        self.char2idx = None
        self.idx2char = None

    def preprocess_text(self, text, sequence_length=40):
        # TODO: Преобразовать текст в последовательности
        # Создать mapping символ -> индекс
        # Генерировать training pairs (input_sequence, target_char)

        # получаем отсортированный список уникальных символов
        vocab = sorted(list(set(text)))
        self.char2idx = {c: i for i, c in enumerate(vocab)}
        self.idx2char = np.array(vocab)
        self.vocab_size = len(vocab)

        # закодировать весь текст
        text_as_int = np.array([self.char2idx[c] for c in text])

        # создаём входные и целевые последовательности
        inputs = []
        targets = []
        for i in range(0, len(text_as_int) - sequence_length):
            inputs.append(text_as_int[i:i + sequence_length])
            targets.append(text_as_int[i + sequence_length])

        X = np.array(inputs)
        y = np.array(targets)
        return X, y

    def compile_and_train(self, X_train, y_train, epochs=50):
        # TODO: Обучить модель
        # Loss: sparse_categorical_crossentropy
        # Optimizer: Adam

        self.model.compile(
            loss='sparse_categorical_crossentropy',
            optimizer='adam',
            metrics=['accuracy']
        )

        # callback для мониторинга
        checkpoint_cb = tf.keras.callbacks.ModelCheckpoint(
            filepath='text_gen_model.keras',
            save_best_only=True,
            monitor='loss'
        )

        history = self.model.fit(
            X_train, y_train,
            batch_size=128,
            epochs=epochs,
            callbacks=[checkpoint_cb]
        )
        return history

    def _sample_with_temperature(self, logits, temperature=1.0):
        # Реализация temperature-based sampling
        logits = np.asarray(logits).astype('float64')
        logits = logits / temperature
        exp = np.exp(logits - np.max(logits))
        probs = exp / np.sum(exp)
        return np.random.choice(len(probs), p=probs)

    def generate_text(self, seed_text, num_chars=100, temperature=1.0):
        # TODO: Генерировать текст из seed
        # Параметр temperature контролирует случайность
        # temperature < 1: более предсказуемо
        # temperature > 1: более разнообразно
        # 1. Закодировать seed_text
        generated = seed_text

        # если словари ещё не заданы, выдадим сообщение
        if self.char2idx is None or self.idx2char is None:
            raise ValueError("Сначала вызовите preprocess_text для подготовки словаря.")

        seed_encoded = [self.char2idx.get(c, 0) for c in seed_text]
        sequence_length = len(seed_encoded)

        for _ in range(num_chars):
            # гарантируем фиксированную длину входа
            if len(seed_encoded) < sequence_length:
                pad = [0] * (sequence_length - len(seed_encoded))
                input_seq = pad + seed_encoded
            else:
                input_seq = seed_encoded[-sequence_length:]

            x = np.array(input_seq)[None, :]  # shape (1, seq_len)

            # 2. Цикл:
            # - Предсказать вероятности следующего символа
            preds = self.model.predict(x, verbose=0)[0]

            # - Применить temperature
            next_index = self._sample_with_temperature(preds, temperature)

            # - Выбрать символ по распределению
            next_char = self.idx2char[next_index]

            # - Добавить в последовательность
            generated += next_char
            seed_encoded.append(next_index)

        return generated


# ===== Загрузка текста книги (public domain, Project Gutenberg) =====
# Используем, например, текст Шекспира.
# Прямая текстовая версия "Complete Works of William Shakespeare". [web:13][web:17]
url = "https://www.gutenberg.org/files/100/100-0.txt"
response = requests.get(url)
raw_text = response.text

# для ускорения можно взять кусок текста
text = raw_text[5000:50000]  # обрезка первых служебных строк и ограничения размера

# ===== Подготовка данных =====
sequence_length = 60

# временный объект только для препроцессинга текста
tmp = TextGenerator(vocab_size=100)
X, y = tmp.preprocess_text(text, sequence_length=sequence_length)

# сохраняем словари и размер алфавита
char2idx = tmp.char2idx
idx2char = tmp.idx2char
vocab_size = tmp.vocab_size

# создаём финальную модель с правильным vocab_size
tg = TextGenerator(vocab_size=vocab_size, embedding_dim=128, lstm_units=128)
tg.char2idx = char2idx
tg.idx2char = idx2char

# ===== Обучение =====
history = tg.compile_and_train(X, y, epochs=10)  # при необходимости увеличить число эпох

# ===== Генерация текста =====
seed = "ROMEO:"  # любой seed на английском
print("Seed:", seed)
print("\nGenerated (T=0.5):\n")
print(tg.generate_text(seed, num_chars=500, temperature=0.5))

print("\nGenerated (T=1.0):\n")
print(tg.generate_text(seed, num_chars=500, temperature=1.0))

print("\nGenerated (T=1.5):\n")
print(tg.generate_text(seed, num_chars=500, temperature=1.5))
