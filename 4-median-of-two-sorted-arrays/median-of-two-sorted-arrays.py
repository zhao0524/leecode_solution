class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0 
        j = 0
        merg = []

        while i < len(nums1) and j < len(nums2):
            if(nums1[i] <= nums2[j]):
                merg.append(nums1[i])
                i = i + 1
            else:
                merg.append(nums2[j])
                j= j + 1
         
        while(i < len(nums1)):
            merg.append(nums1[i])
            i = i+1
        
        while(j < len(nums2)):
            merg.append(nums2[j])
            j = j+1

        if(len(merg)%2 == 1 ):
            return merg[len(merg)//2]
        else:
            return (merg[len(merg)//2-1] + merg[len(merg)//2])/2