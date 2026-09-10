import os, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
print("ROOT:", ROOT)
print("sys.path[0:3]:", sys.path[0:3])

if ROOT not in sys.path:
    sys.path.insert(0, ROOT)


from environment.camera_environment import CameraEnvironment

def main():
    env = CameraEnvironment()

    try:
        # 10 step
        for i in range(10):
            out = env.step()
            print(out)
    
    finally:
        env.close()

if __name__ == "__main__":
    main()
