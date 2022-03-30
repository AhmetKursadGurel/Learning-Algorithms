class Point:
    def __init__(self, p_x, p_y):
        self.x = p_x
        self.y = p_y
    
    def distance(self, P2):
        P2[0] = int(P2[0])
        P2[1] = int(P2[1])
        dist=(((self.x-P2[0])**2)+((self.y-P2[1])**2))**(1/2)
        return dist


    def closer(self, P2, P3):
        if self.distance(P2)== self.distance(P3):
            return P2,P3


        elif self.distance(P2) < self.distance(P3):
            return P2
        else:
            return P3
        

    def __str__(self):
        emtystr=f"({self.x},{self.y})"
        return emtystr
        
        