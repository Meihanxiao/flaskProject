import sys
import  os 
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

from script.calculate import avg

def test_for_calculate():

    avgp = avg(target = [35, 38])
    print(avgp)

if __name__ == "__main__":
    test_for_calculate()
