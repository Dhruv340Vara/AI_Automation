from __future__ import annotations

from automation.triggers.file_trigger import FileTrigger


class FolderTrigger(FileTrigger):
    """
    Folder monitoring trigger.

    Uses FileWatcher internally.
    """

    def __init__(
        self,
        name: str,
        path: str,
        recursive: bool = True,
        extensions: list[str] | None = None,
        ignore_hidden: bool = True,
    ):

        super().__init__(
            name=name,
            path=path,
            events=[
                "created",
                "modified",
                "deleted",
                "renamed",
            ],
            recursive=recursive,
            extensions=extensions,
            ignore_hidden=ignore_hidden,
        )

    def __repr__(self):

        return (
            "<FolderTrigger "
            f"{self.name} "
            f"path={self.path}>"
        )
