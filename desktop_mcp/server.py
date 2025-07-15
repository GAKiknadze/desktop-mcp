from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from typing import Tuple

from mcp.server.fastmcp import Context, FastMCP

from . import context, core


@asynccontextmanager
async def app_lifespan(server: FastMCP) -> AsyncIterator[context.AppContext]:
    yield context.AppContext(
        keyboard=core.KeyboardController(),
        mouse=core.MouseController(),
        # screen=core.ScreenController(),
        # system=core.SystemController(),
        # window=core.WindowController()
    )


mcp = FastMCP("Desktop MCP Server", stateless_http=True, lifespan=app_lifespan)

# Keyboard


@mcp.tool(title="Keyboard | Write", description="")
async def keyboard_write(text: str, ctx: Context, interval: float = 0) -> None:
    keyboard: core.KeyboardController = ctx.request_context.lifespan_context.keyboard
    keyboard.write(text=text, interval=interval)
    await ctx.debug(f"Text writed: `{text}`")


@mcp.tool(title="Keyboard | Press", description="")
async def keyboard_press(key: str, ctx: Context) -> None:
    keyboard: core.KeyboardController = ctx.request_context.lifespan_context.keyboard
    keyboard.press(key=key)
    await ctx.debug(f"Key pressed: `{key}`")


@mcp.tool(title="Keyboard | Key Down", description="")
async def keyboard_key_down(key: str, ctx: Context) -> None:
    keyboard: core.KeyboardController = ctx.request_context.lifespan_context.keyboard
    keyboard.key_down(key=key)
    await ctx.debug(f"Key down: `{key}`")


@mcp.tool(title="Keyboard | Key Up", description="")
async def keyboard_key_up(key: str, ctx: Context) -> None:
    keyboard: core.KeyboardController = ctx.request_context.lifespan_context.keyboard
    keyboard.key_up(key=key)
    await ctx.debug(f"Key up: `{key}`")


# Mouse


@mcp.tool(title="Mouse | Position", description="Current mouse position x and y")
async def mouse_position(ctx: Context) -> Tuple[int, int]:
    mouse: core.MouseController = ctx.request_context.lifespan_context.mouse
    x, y = mouse.position()
    await ctx.debug(f"Mouse position: `{x, y}`")
    return x, y


@mcp.tool(title="Mouse | Move to", description="Move mouse to XY coordinates")
async def mouse_move_to(x: int, y: int, ctx: Context) -> None:
    mouse: core.MouseController = ctx.request_context.lifespan_context.mouse
    mouse.move_to(x, y)
    await ctx.debug(f"Move to: `{x, y}`")


@mcp.tool(
    title="Mouse | Move rel", description="Move mouse relative to its current position"
)
async def mouse_move_rel(x: int, y: int, ctx: Context) -> None:
    mouse: core.MouseController = ctx.request_context.lifespan_context.mouse
    mouse.move_rel(x, y)
    await ctx.debug(f"Move rel: `{x, y}`")


@mcp.tool(title="Mouse | Drag to", description="Drag mouse to XY")
async def mouse_drag_to(x: int, y: int, ctx: Context) -> None:
    mouse: core.MouseController = ctx.request_context.lifespan_context.mouse
    mouse.drag_to(x, y)
    await ctx.debug(f"Drag to: `{x, y}`")


@mcp.tool(
    title="Mouse | Drag rel", description="Drag mouse relative to its current position"
)
async def mouse_drag_rel(x: int, y: int, ctx: Context) -> None:
    mouse: core.MouseController = ctx.request_context.lifespan_context.mouse
    mouse.drag_rel(x, y)
    await ctx.debug(f"Drag rel: `{x, y}`")


@mcp.tool(title="Mouse | Right click", description="Mouse right click")
async def mouse_right_click(
    ctx: Context, x: int | None = None, y: int | None = None
) -> None:
    mouse: core.MouseController = ctx.request_context.lifespan_context.mouse
    mouse.right_click(x, y)
    await ctx.debug(f"Right click: `{x, y}`")


@mcp.tool(title="Mouse | Left click", description="Mouse left click")
async def mouse_left_click(
    ctx: Context, x: int | None = None, y: int | None = None
) -> None:
    mouse: core.MouseController = ctx.request_context.lifespan_context.mouse
    mouse.left_click(x, y)
    await ctx.debug(f"Left click: `{x, y}`")


@mcp.tool(title="Mouse | Left double click", description="Mouse left double click")
async def mouse_left_double_click(
    ctx: Context, x: int | None = None, y: int | None = None
) -> None:
    mouse: core.MouseController = ctx.request_context.lifespan_context.mouse
    mouse.left_double_click(x, y)
    await ctx.debug(f"Left double click: `{x, y}`")


@mcp.tool(title="Mouse | Middle click", description="Mouse middle click")
async def mouse_middle_click(
    ctx: Context, x: int | None = None, y: int | None = None
) -> None:
    mouse: core.MouseController = ctx.request_context.lifespan_context.mouse
    mouse.middle_click(x, y)
    await ctx.debug(f"Middle click: `{x, y}`")


@mcp.tool(
    title="Mouse | Scroll",
    description="Positive scrolling will scroll up, negative scrolling will scroll down",
)
async def mouse_scroll(
    amount_to_scroll: float, ctx: Context, x: int | None = None, y: int | None = None
) -> None:
    mouse: core.MouseController = ctx.request_context.lifespan_context.mouse
    mouse.scroll(amount_to_scroll, x, y)
    await ctx.debug(f"Scroll: `{amount_to_scroll, x, y}`")
