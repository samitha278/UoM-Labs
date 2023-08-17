import math

def main():

    data = readFile(input().strip())
    if data is None:return -1

    mass = data["mass"]
    weights =  [getWeight(mass,planet) for planet in data["planets"]]

    if writer("results.txt",weights)==-1:return -1




def writer(outFile,output):
    try:
        with open(outFile,"w") as file:
            for data in output:
                l = len(data[0])
                x = 15-l
                line = f"mass in {data[0]} "+ " "*x + f" weight is {data[1]} N"
                
                print(line)
                file.write(line+"\n")

    except:
        return -1
    





def getWeight(mass,planet):

    radius = planet["radius"]
    density = planet["density"]

    massPlanet = getPlanetMass(radius,density)

    G = 6.67*(10**(-11))
    
    weight = (G * mass * massPlanet )/(radius**2)

    return (planet["planetName"],weight)




def getPlanetMass(radius,density):

    volume = getPlanetVolume(radius)

    mass = volume*density

    return mass



def getPlanetVolume(radius):

    volume = (4*(math.pi)*(radius**3))/3
    return volume






def readFile(inpFile):

    try:
        with open(inpFile) as file:
            mass,N = list(map(int,file.readline().rstrip().split()))

            planets = []
            for line in file:
                planetName,*details =line.rstrip().split()
                radius,density = list(map(int,details)) 

                planets.append({"planetName":planetName,"radius":radius,"density":density})


    except Exception as e:
        print(e)
        return
    
    return {"mass":mass,"planets":planets}





main()
