from cx_Freeze import setup, Executable

setup(
    name = "zzz_auto_daily_tool",
    version = "0.0.1",
    description = "ZZZ Auto Daily Tool",
    executables = [Executable("ZzzAutoDailyTool/__main_.py")]
)
