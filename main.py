import os
import glob
from pydub import AudioSegment

src_folder = "dataset"
dst_folder = "bublik"

# Получаем список всех ogg файлов в папке
ogg_files = glob.glob(os.path.join(src_folder, "*.ogg"))

# Перебираем каждый ogg файл
for ogg_file in ogg_files:
    # Извлекаем базовое имя файла без расширения
    basename = os.path.basename(ogg_file)[:-4]

    # Формируем имя выходного файла wav
    wav_file = os.path.join(dst_folder, basename + ".wav")

    # Конвертируем в wav
    sound = AudioSegment.from_ogg(ogg_file)
    sound.export(wav_file, format="wav")

print("Конвертация завершена!")