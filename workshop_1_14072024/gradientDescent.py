import numpy as np

def func(x):
            return np.sin(x)
        
def grad(x):
            return np.cos(x)

x_init = np.pi / 2 + 1
y_init = func(x_init)

for _ in range(10):
        grad_value = grad(x_init)
        

        # Gradient descent step
        new_x = x_init - 0.01 * grad_value
        new_y = func(new_x)

        # Update ball position
        new_position = (new_x, new_y)
        # ball.move_to(new_position)
        print(new_position)

        # Update path
        # new_path = path.copy()
        # new_path.add_points_as_corners([new_position])
        # self.play(Transform(path, new_path), run_time=0.05)
        
        # Update current position
        x_init = new_x
        y_init = new_y