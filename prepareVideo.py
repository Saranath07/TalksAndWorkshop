from manim import *

class GradientDescent(Scene):
    def construct(self):
        # Define the function and its gradient
        def func(x):
            return x**2
        
        def grad(x):
            return 2*x
        
        # Create axes
        axes = Axes(
            x_range=[-6, 6, 1],
            y_range=[0, 30, 5],
            axis_config={"color": BLUE}
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="f(x)")
        
        # Plot the function
        graph = axes.plot(func, color=WHITE)
        graph_label = axes.get_graph_label(graph, label="x^2")

        # Initial positions
        x_init_pos = 5
        x_init_neg = -5

        # Create balls
        ball_pos = Dot(color=GREEN).move_to(axes.c2p(x_init_pos, func(x_init_pos)))
        ball_neg = Dot(color=RED).move_to(axes.c2p(x_init_neg, func(x_init_neg)))

        # Path to trace the ball's movement
        path_pos = VMobject()
        path_pos.set_points_as_corners([ball_pos.get_center(), ball_pos.get_center()])
        path_neg = VMobject()
        path_neg.set_points_as_corners([ball_neg.get_center(), ball_neg.get_center()])

        # Add components to the scene
        self.add(axes, axes_labels, graph, graph_label, ball_pos, ball_neg, path_pos, path_neg)

        # Add equations to the scene
        eq1 = MathTex(r"f(x) = x^2").to_corner(UL).scale(0.7)
        eq2 = MathTex(r"f'(x) = 2x").next_to(eq1, DOWN).scale(0.7)
        self.add(eq1, eq2)

        # Initial gradient and value equations
        grad_eq_pos = MathTex(f"f'(x_{{pos}}) = 2*{x_init_pos} = {2*x_init_pos}").to_corner(DL).scale(0.6)
        grad_eq_neg = MathTex(f"f'(x_{{neg}}) = 2*{x_init_neg} = {2*x_init_neg}").next_to(grad_eq_pos, DOWN).scale(0.6)
        value_eq_pos = MathTex(f"f(x_{{pos}}) = {x_init_pos}^2 = {func(x_init_pos)}").next_to(eq2, DOWN).scale(0.6)
        value_eq_neg = MathTex(f"f(x_{{neg}}) = {x_init_neg}^2 = {func(x_init_neg)}").next_to(value_eq_pos, DOWN).scale(0.6)
        self.add(grad_eq_pos, grad_eq_neg, value_eq_pos, value_eq_neg)

        # Gradient descent steps
        for _ in range(5):
            # For x = 5
            grad_value_pos = grad(x_init_pos)
            new_x_pos = x_init_pos - 0.2 * grad_value_pos  # Step size 0.2
            new_y_pos = func(new_x_pos)
            new_position_pos = axes.c2p(new_x_pos, new_y_pos)
            ball_pos.move_to(new_position_pos)
            path_pos.add_points_as_corners([new_position_pos])
            
            # For x = -5
            grad_value_neg = grad(x_init_neg)
            new_x_neg = x_init_neg - 0.2 * grad_value_neg  # Step size 0.2
            new_y_neg = func(new_x_neg)
            new_position_neg = axes.c2p(new_x_neg, new_y_neg)
            ball_neg.move_to(new_position_neg)
            path_neg.add_points_as_corners([new_position_neg])

            # Update equations
            new_grad_eq_pos = MathTex(f"f'(x_{{pos}}) = 2*{new_x_pos:.2f} = {2*new_x_pos:.2f}").to_corner(DL).scale(0.6)
            new_grad_eq_neg = MathTex(f"f'(x_{{neg}}) = 2*{new_x_neg:.2f} = {2*new_x_neg:.2f}").next_to(new_grad_eq_pos, DOWN).scale(0.6)
            new_value_eq_pos = MathTex(f"f(x_{{pos}}) = {new_x_pos:.2f}^2 = {new_y_pos:.2f}").next_to(eq2, DOWN).scale(0.6)
            new_value_eq_neg = MathTex(f"f(x_{{neg}}) = {new_x_neg:.2f}^2 = {new_y_neg:.2f}").next_to(new_value_eq_pos, DOWN).scale(0.6)

            self.play(
                ball_pos.animate.move_to(new_position_pos),
                ball_neg.animate.move_to(new_position_neg),
                Create(path_pos),
                Create(path_neg),
                Transform(grad_eq_pos, new_grad_eq_pos),
                Transform(grad_eq_neg, new_grad_eq_neg),
                Transform(value_eq_pos, new_value_eq_pos),
                Transform(value_eq_neg, new_value_eq_neg),
                run_time=2
            )
            
            # Update current positions
            x_init_pos = new_x_pos
            x_init_neg = new_x_neg
        
        self.wait(2)

if __name__ == "__main__":
    from manim import config
    config.media_width = "1920x1080"
    config.frame_rate = 60
    config.background_color = BLACK
    scene = GradientDescent()
    scene.render()
