import os
import wave
import math

for file in os.listdir('./wav'):
    basename, ext = os.path.splitext(file)
    if ext == '.wav':
        # セグメントを取得する
        segments = list()
        with open(f'./wav/{basename}.lab', 'r') as lab:
            for line in lab:
                columns = line.strip().split(' ')
                if columns[2] == 'silB' or columns[2] == 'silE':
                    continue

                segments.append((float(columns[0]), float(columns[1])))

        # 出力先のディレクトリを作成する
        if not os.path.exists(f'./result/{basename}'):
            os.mkdir(f'./result/{basename}')

        # 音声ファイルを読み込む
        whole = wave.open(f'./wav/{basename}.wav', 'r')
        fs = whole.getframerate()

        # 音声を分割して出力する
        for n, (begin, end) in enumerate(segments):
            whole.setpos(math.floor(begin * fs))
            frames = whole.readframes(math.ceil((end - begin) * fs))

            with wave.open(f'./result/{basename}/{n}.wav', 'w') as seg:
                seg.setnchannels(whole.getnchannels())
                seg.setsampwidth(whole.getsampwidth())
                seg.setframerate(whole.getframerate())
                seg.writeframes(frames)