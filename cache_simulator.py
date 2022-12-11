import random

class Memory:
    def __init__(self, memoryData):
        self.memStore = memoryData

# Cache 클래스, replacing policy는 가장 적게 쓴 원소 삭제
class Cache:
    def __init__(self):
        self.cacheStore = [0] * 20
        self.numOfUsed = [0] * 20
        self.index = 0
        self.isFull = False
        self.hit = 0

    # 가장 적게 읽어진 원소의 index 찾는 함수
    def findLeastUsedIndex(self):
        minIndex = 0
        for i in range(0, 20):
            if self.numOfUsed[i] < self.numOfUsed[minIndex]:
                minIndex = i

        return minIndex

    def readData(self, memoryData):
        for i in range(0, 100): # memoryData 읽는 루프
            # cache 다 안찼을 때
            if not self.isFull:
                if memoryData[i] not in self.cacheStore:
                    self.cacheStore[self.index] = memoryData[i]
                    self.numOfUsed[self.index] += 1
                    self.index += 1
                    if self.index == 20:
                        self.isFull = True
                else:
                    overlapIndex = self.cacheStore.index(memoryData[i])
                    self.numOfUsed[overlapIndex] += 1
                    self.hit += 1
            # cache 다 찼을때
            else:
                if memoryData[i] not in self.cacheStore:    # 읽는 데이터가 캐시에 없으면 하나 바꿔야함
                    minIndex = self.findLeastUsedIndex()
                    self.cacheStore[minIndex] = memoryData[i]
                    self.numOfUsed[minIndex] = 1
                else:
                    overlapIndex = self.cacheStore.index(memoryData[i])
                    self.numOfUsed[overlapIndex] += 1

    def printHit(self):
        print("hit 한 수: ", self.hit)


### test code ###
programData = random.choices(range(1, 50), k=100)   # 가상 program의 data
memory = Memory(programData)                        # memory에 program data 올림
cache = Cache()                                     # cache 객체 생성

cache.readData(memory.memStore)                     # memory의 data 읽기
cache.printHit()                                    # cache 성능 확인


