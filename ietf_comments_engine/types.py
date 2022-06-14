from typing import Tuple

CommentType = Tuple[str, str]


class Ui:
    """
    Abstract class for a UI.
    """

    def status(self, name: str, value: str) -> None:
        """Informational statement."""
        pass

    def warn(self, message: str, source: str = "") -> None:
        """Warning."""
        pass

    def error(self, message: str, source: str = "") -> None:
        """Error"""
        pass

    def comment(self, comment: CommentType) -> None:
        """The content of a review comment."""
        pass
