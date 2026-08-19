class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        paper_counts = [0] * (n + 1) 

        for c in citations:
            paper_counts[min(n, c)] += 1 # agar citations array ke index se bara hua, to jo index last wala hoga vo wali citation us index me dal jaegi for eg: array ki length 6 hai to jo citations 6 se zyada honge vo 6 me add hojaenge

        h = n #hume max H index nikalna hai jo ki n k size ke equal ho skta h

        papers = paper_counts[n]

        while papers < h:
            h -= 1
            papers += paper_counts[h]
        return h
