"""simple_screen_tasks.py"""

# Script written by @dbiersach (simple_screen.py):
# https://github.com/dbiersach/qis101/blob/0aa4537a02ac7f71d62ce6bbaf54e1e3175a5d51/labs/Session%2019%20-%20Dynamical%20Systems/simple_screen.py
# Called as helper script in ifs_hexagonal.py

from __future__ import annotations

import typing
from typing import Any

import pygame
from pygame import Color

if typing.TYPE_CHECKING:
    import numpy as np
    from typing import Callable
    from numpy.typing import NDArray
    from pygame import Surface


class SimpleScreen:
    def __init__(
        self,
        world_rect: tuple[tuple[float, float], tuple[float, float]],
        screen_size: tuple[int, int] = (500, 500),
        draw_function: Callable[..., Any] = ...,  # type: ignore
        event_function: Callable[..., Any] = ...,  # type: ignore
        title: str = "",
        background_color: Color = Color("black"),
        zoom_rect_color: Color = Color("white"),
    ) -> None:
        pygame.init()
        pygame.display.set_mode(screen_size)
        pygame.display.set_caption(title)
        self.surface: Surface = pygame.display.get_surface()
        self.background_color: Color = background_color

        self.draw_function: Callable[[Any], Any] = draw_function
        self.event_function: Callable[[Any], Any] = event_function

        self.screen_size: tuple[int, int] = screen_size
        self.screen_width: int = screen_size[0] - 1
        self.screen_height: int = screen_size[1] - 1
        self.screen_ratio: float = self.screen_width / self.screen_height

        self.world_rects: list[tuple[tuple[float, float], tuple[float, float]]] = []
        self.world_rects.append(world_rect)
        self.calc_world_rect()

        self.is_zooming = False
        self.zoom_pos_start: tuple[float, float] = (0.0, 0.0)
        self.zoom_pos_stop: tuple[float, float] = (0.0, 0.0)
        self.zoom_surface: Surface
        self.zoom_rect_color = Color(zoom_rect_color)

    def calc_world_rect(self) -> None:
        self.wx1: float = self.world_rects[-1][0][0]
        self.wy1: float = self.world_rects[-1][0][1]
        self.wx2: float = self.world_rects[-1][1][0]
        self.wy2: float = self.world_rects[-1][1][1]

        self.world_min: tuple[float, float] = (self.wx1, self.wy1)
        self.world_max: tuple[float, float] = (self.wx2, self.wy2)

        self.world_width: float = self.wx2 - self.wx1
        self.world_height: float = self.wy2 - self.wy1

        # Set aspect ratios (rw = ratio width, rh = ratio height)
        self.rw: float = self.screen_width / self.world_width
        self.rh: float = self.screen_height / self.world_height

    def screen_x(self, wx: float) -> float:
        return round(self.rw * (wx - self.wx1))

    def screen_y(self, wy: float) -> float:
        return round(self.rh * (wy - self.wy1))

    def world_x(self, sx: int) -> float:
        return self.wx1 + sx / self.rw

    def world_y(self, sy: int) -> float:
        return self.wy1 + sy / self.rh

    def set_background(self, clr: Color) -> None:
        self.surface.fill(clr)

    def set_title(self, title: str) -> None:
        pygame.display.set_caption(title)

    def set_screen_pixel(self, sx: float, sy: float, clr: Color) -> None:
        if sx >= 0 and sx <= self.screen_width and sy >= 0 and sy <= self.screen_height:
            # Note: first three values in clr are the R, G, B components
            self.pixels[sx, self.screen_height - sy] = clr[:3]

    def set_world_pixel(self, wx: float, wy: float, clr: Color) -> None:
        sx: float = self.screen_x(wx)
        sy: float = self.screen_y(wy)
        self.set_screen_pixel(sx, sy, clr)

    def flip(self) -> None:
        pygame.display.flip()

    def update(self) -> None:
        self.set_background(self.background_color)
        self.pixels: NDArray[np.float_] = pygame.surfarray.pixels3d(self.surface)
        if self.draw_function is not Ellipsis:  # type: ignore
            self.draw_function(self)
        self.surface.unlock()
        del self.pixels
        pygame.display.flip()

    def create_zoom_rect(self, event: Any) -> pygame.Rect:
        self.zoom_pos_stop = event.pos
        zoom_width: float = self.zoom_pos_stop[0] - self.zoom_pos_start[0]
        zoom_height: float = self.zoom_pos_stop[1] - self.zoom_pos_start[1]
        zoom_rect = pygame.Rect((self.zoom_pos_start, (zoom_width, zoom_height)))
        zoom_rect.normalize()
        # Ensure zoom rect preserves screen aspect ratio
        zoom_rect.width = int(self.screen_ratio * zoom_rect.height)
        return zoom_rect

    def show(self) -> None:
        # Show the screen at least once
        self.update()
        # Enter game loop
        running = True
        while running:
            event: pygame.event.Event
            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:  # noqa: SIM102
                    # Check if left button is being held down
                    if event.buttons[0] == 1:  # LEFT BUTTON
                        if not self.is_zooming:
                            self.is_zooming = True
                            self.zoom_pos_start = event.pos
                            self.zoom_pos_stop = (0, 0)
                            self.zoom_surface = self.surface.copy()
                            # Save current image before start of zoom
                            self.zoom_surface.blit(self.surface, (0, 0))
                        else:
                            # Restore image before start of zoom
                            self.surface.blit(self.zoom_surface, (0, 0))
                            # Construct the new zoom rectangle
                            zoom_rect: pygame.Rect = self.create_zoom_rect(event)
                            # Draw the new zoom rect
                            pygame.draw.rect(
                                self.surface, self.zoom_rect_color, zoom_rect, 3
                            )
                            pygame.display.flip()
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:  # LEFT BUTTON  # noqa: SIM102
                        if self.is_zooming:
                            self.is_zooming = False
                            # Restore image before start of zoom
                            self.surface.blit(self.zoom_surface, (0, 0))
                            # Calculate new world rectangle
                            zoom_rect = self.create_zoom_rect(event)
                            if zoom_rect.width > 0 and zoom_rect.height > 0:
                                new_wx1: float = self.world_x(zoom_rect.left)
                                new_wy1: float = self.world_y(
                                    self.screen_height
                                    - (zoom_rect.top + zoom_rect.height)
                                )
                                new_wx2: float = self.world_x(
                                    zoom_rect.left + zoom_rect.width
                                )
                                new_wy2: float = self.world_y(
                                    self.screen_height - zoom_rect.top
                                )
                                # Push new world rectangle onto stack
                                self.world_rects.append(
                                    ((new_wx1, new_wy1), (new_wx2, new_wy2))
                                )
                                # Redraw world using this new world rectangle
                                self.calc_world_rect()  #
                                self.update()
                    if event.button == 3:  # RIGHT BUTTON  # noqa: SIM102
                        # Restore prior zoom state
                        if len(self.world_rects) > 1:
                            self.world_rects.pop()
                            self.calc_world_rect()
                            self.update()
                # Allow client to handle events
                if self.event_function is not Ellipsis:  # type: ignore
                    self.event_function(self, event)  # type: ignore
                if event.type == pygame.QUIT:
                    running = False
        pygame.quit()
