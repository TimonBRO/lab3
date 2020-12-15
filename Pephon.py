import numpy as np
class MyClass():
    def Progression(self,b,q,n):
        self.b=b
        self.q=q
        self.n=n
        a= np.zeros(shape=[n])
        i=0
        while(i<n):
            b*=q
            i+=1
            a[i-1]=b
        return a
    def Return_k(self,a,k):
        ku=0
        i=0
        while(i<self.n):
            self.b*=self.q
            if(i<k)&(k<self.n):
                ku+=self.b
            i+=1
            a[i-1]=self.b
        return(ku)
    def presenceElement(self,j,a):
        if (j in a):
           print ('True')
        else:
           print ('False')

        return (j in a)
    def elemReturn(self,c,a):
        print(a[c])
        return a[c] 
