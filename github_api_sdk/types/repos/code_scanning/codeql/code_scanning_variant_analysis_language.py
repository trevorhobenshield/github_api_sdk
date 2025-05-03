

from typing_extensions import Literal, TypeAlias

__all__ = ["CodeScanningVariantAnalysisLanguage"]

CodeScanningVariantAnalysisLanguage: TypeAlias = Literal[
    "cpp", "csharp", "go", "java", "javascript", "python", "ruby", "rust", "swift"
]
