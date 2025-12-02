from camera_controller import CameraController
from image_analyzer import ImageAnalyzer 
from rl_agent import RLAgent


class CameraEnvironment:

    def __init__(self):
        self.camera = CameraController()
        self.analyzer = ImageAnalyzer()


    
        actions = [
            {"exposure": 1000},
            {"exposure": 2000},
            {"exposure": 3000}
        ]

        self.agent = RLAgent(actions)
        self.step_count = 0

        

    def step(self):

        self.step_count += 1

        image = self.camera.capture_image()

        features = self.anaylzer.extract_features(image)

        defect_prob = self.analyzer.compute_defect_probability(features)

        action = self.rl_agent.choose_action(features)

        self.camera.set_parameters(**action)

        image2 = self.camera.capture_image()

        features2 = self.analyzer.extract_features(image2)

        defect_prob2 = self.analyzer.compute_defect_probability(features2)

        reward = self._caculate_reward(defect_prob2)

        self.rl_agent.learn(features, action, reward, next_state= features2)

        info = {
            "step": self.step_count,
            "defect_prob": defect_prob,
            "reward": reward,
            "action": action
        }

        return info
    
    

    def _calculate_reward(self, defect_prob):
        return defect_prob*10
    

    def reset(self):
        self.step_count = 0
        print("Environment reset")

    
    def close(self):
        self.camera.close()
        print("Environment closed")

        