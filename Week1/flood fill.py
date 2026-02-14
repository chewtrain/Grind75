class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        maxr=len(image) #number of rows
        maxc=len(image[0]) #number of columns
        oricolor=image[sr][sc] #original color of starting pixel
        if color==oricolor: #if the new color is same as original color, just return the image as is
            return image
        self.changecolor(image,sr,sc,maxr,maxc,oricolor,color)
        return image 
        #within floodFill we call a function to change the image, and then we use floodFill to return the updated image
        #shouldn't use floodFill as the function to change the image because we will overcomplicate floodFill
        
    def changecolor(self,image,r,c,maxr,maxc,oricolor,color): #this is the function that actually does the changing of image
        if image[r][c]==oricolor: #if the color at the pixel image[r][c] = original color of starting pixel, change color of pixel to new color 
            image[r][c]=color #note that the following if statements are same indent as this line. means we only change adjacent pixels if a pixel gets changed 
            if r>0:
                self.changecolor(image,r-1,c,maxr,maxc,oricolor,color)
            if r+1<maxr: #need r+1 because of 0 indexing 
                self.changecolor(image,r+1,c,maxr,maxc,oricolor,color)
            if c>0:
                self.changecolor(image,r,c-1,maxr,maxc,oricolor,color)
            if c+1<maxc: #need c+1 because of 0 indexing 
                self.changecolor(image,r,c+1,maxr,maxc,oricolor,color)
        return None #if a pixel is not changed, we don't change adjacent pixels to that pixel 