from manim import *

class TestLorenzAttractor3D(ThreeDScene):
    def construct(self):
        # Добавляем оси
        axes = ThreeDAxes(
            x_range=[-10, 10],
            y_range=[-10, 10],
            z_range=[-6, 6],
            x_length=10,
            y_length=10,
            z_length=6
        )
        self.add(axes)

        # Устанавливаем ориентацию камеры
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        # Начинаем вращение камеры
        self.begin_ambient_camera_rotation(rate=0.1)

        # Начальные условия для системы Лоренца
        x, y, z = 10, 10, 10
        a, b, c = 10, 28, 8 / 3
        dt = 0.0005
        num_steps = 10000

        # Массив для хранения точек траектории
        trajectory_points = []

        # Численное интегрирование системы Лоренца
        for _ in range(num_steps):
            dx = (a * (y - x)) * dt
            dy = (x * (b - z) - y) * dt
            dz = (x * y - c * z) * dt

            x += dx
            y += dy
            z += dz

            trajectory_points.append([x / 12, y / 12, z / 12])

        # Создаем траекторию как параметрическую функцию
        trajectory_curve = ParametricFunction(
            lambda t: trajectory_points[int(t * (num_steps - 1))],
            t_range=[0, 1],
            color=RED
        )

        # Анимация для создания траектории
        self.play(Create(trajectory_curve), run_time=10, rate_func=linear)

        '''
        # Создаем точку, которая будет двигаться по траектории
        moving_dot = Dot3D(point=trajectory_points[0], radius=0.1, color=YELLOW)
        self.add(moving_dot)

        # Анимация точки вдоль траектории
        self.play(MoveAlongPath(moving_dot, trajectory_curve), run_time=5, rate_func=linear)
        '''

class LorenzAttractor3D(ThreeDScene):
    def construct(self):
        # Добавляем оси
        axes = ThreeDAxes(
            x_range=[-10, 10],
            y_range=[-10, 10],
            z_range=[-6, 6],
            x_length=10,
            y_length=10,
            z_length=6
        )
        self.add(axes)

        # Устанавливаем ориентацию камеры
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        # Начинаем вращение камеры
        self.begin_ambient_camera_rotation(rate=0.1)

        # Начальные условия для системы Лоренца
        a, b, c = 10, 28, 8 / 3
        dt = 0.0005
        num_steps = 10000
        
        # Функция для численного интегрирования системы Лоренца
        def lorenz_trajectory(x_start, y_start, z_start):
            x, y, z = x_start, y_start, z_start
            trajectory_points = []

            for _ in range(num_steps):
                dx = (a * (y - x)) * dt
                dy = (x * (b - z) - y) * dt
                dz = (x * y - c * z) * dt

                x += dx
                y += dy
                z += dz

                trajectory_points.append([x / 12, y / 12, z / 12])
            return trajectory_points

        # Список начальных условий для нескольких траекторий
        initial_conditions = [
            (10, 10, 10),
            (8, 9, 10),
            (10, 9, 8),
            (12, 12, 12)
        ]

        # Список цветов для разных траекторий
        colors = [RED, BLUE, GREEN, YELLOW]

        # Список для хранения всех траекторий
        trajectories = []

        for i, (x0, y0, z0) in enumerate(initial_conditions):
            trajectory_points = lorenz_trajectory(x0, y0, z0)

            # Создаем траекторию как параметрическую функцию
            trajectory_curve = ParametricFunction(
                lambda t, trajectory_points=trajectory_points: trajectory_points[int(t * (num_steps - 1))],
                t_range=[0, 1],
                color=colors[i]
            )

            trajectories.append(trajectory_curve)

        # Анимация для создания всех траекторий
        self.play(*[Create(trajectory) for trajectory in trajectories], run_time=10, rate_func=linear)