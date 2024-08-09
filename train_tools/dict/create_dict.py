import Preprocess
from tensorflow.keras import preprocessing
import pickle
import pandas as pd

# 말뭉치 데이터 읽어오기
Q = pd.read_csv("../../c_question.csv")
A = pd.read_csv("../../c_answer.csv")
Q.dropna(inplace=True)
A.dropna(inplace=True)

text1 = list(Q['question'])
text2 = list(A['answer'])
corpus_data = text1 + text2
# corpus_data = text1 + text2 + text3 + text4

# 말뭉치 데이터에서 키워드만 추출해서 사전 리스트 생성
p = Preprocess()
dict = []
cnt=[]
for c in corpus_data:
    pos = p.pos(c)
    # print(len(pos))
    cnt.append(len(pos))
    for k in pos:
        dict.append(k[0])

# 사전에 사용될 word2index 생성
# 사전의 첫 번째 인덱스에는 OOV 사용
tokenizer = preprocessing.text.Tokenizer(oov_token='OOV', num_words=100000)
tokenizer.fit_on_texts(dict)
word_index = tokenizer.word_index
print(len(word_index))

# 사전 파일 생성
f = open("chatbot_dict.bin", "wb")
try:
    pickle.dump(word_index, f)
except Exception as e:
    print(e)
finally:
    f.close()