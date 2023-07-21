import sys
import MeCab

def main():
  args = sys.argv
  text = args[1] if len(args) > 1 else None;
  if not text:
    print('[Error] 引数が入力されていません。')
    return

  mecab = MeCab.Tagger("-d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd")
  analizedText = mecab.parse(text)
  print(analizedText)

  print('分析結果: ', execute(analizedText.splitlines()))


def execute(morphemes):
  words = []
  del morphemes[-1];
  isSkipSurface = False;

  for i, v in enumerate(morphemes):
    if isSkipSurface:
      isSkipSurface = False;
      continue;
    currentItem = v.split(',')
    currentSurface, currentPoc = currentItem[0].split('\t')
    currentPocDetail = currentItem[1]

    if i != 0:
      prevItem = morphemes[i - 1].split(',')
      prevSurface, prevPoc = prevItem[0].split('\t')
      prevPocDetail = prevItem[1]

    if i != len(morphemes) - 1:
      nextItem = morphemes[i + 1].split(',')
      nextSurface, nextPoc = nextItem[0].split('\t')
      nextPocDetail = nextItem[1]

    if currentPoc == '記号':
      continue

    if currentPoc == '名詞':
      if currentPocDetail == '数':
        if nextPocDetail == '接尾':
          words.append(currentSurface + nextSurface)
          isSkipSurface = True;
          continue;
        elif prevPocDetail == '固有名詞':
          del words[-1]
          words.append(prevSurface + currentSurface);
          continue;
      if nextPoc == '名詞':
          words.append(currentSurface + nextSurface)
          isSkipSurface = True;
          continue;

    if currentPoc == '動詞':
      if nextPoc == '助動詞':
        words.append(currentSurface + nextSurface)
        isSkipSurface = True;
        continue;


    words.append(currentSurface);
    continue;

  return words

main()
