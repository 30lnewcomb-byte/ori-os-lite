"""Known resource profile for the current Render deployment."""

from dataclasses import dataclass


@dataclass(frozen=True)
class RenderInstanceProfile:
    """Resource limits OriOS Lite must design around on its Render host."""

    cpu_cores: float = 0.1
    memory_mb: int = 512
    name: str = "render-0.1cpu-512mb"


CURRENT_RENDER_INSTANCE = RenderInstanceProfile()

# Keep these as explicit constants so scheduling and sandbox planning can
# account for the host capacity rather than assuming a larger machine.
RENDER_CPU_CORES = CURRENT_RENDER_INSTANCE.cpu_cores
RENDER_MEMORY_MB = CURRENT_RENDER_INSTANCE.memory_mb
