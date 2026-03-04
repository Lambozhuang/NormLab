# NormLab

## Overview
NormLab is an automated utility designed to streamline the grading and file organization process for batch student laboratory submissions. Instructors and teaching assistants typically download bulk archive files containing student submissions from a Learning Management System (LMS). These archives are often cluttered with deeply nested folders, unnecessary OS-generated files (e.g., `__MACOSX`, `.DS_Store`), and inconsistently named documents.

NormLab automatically extracts, cleans up, renames, and flattens these submissions, standardizing them into a clean, easy-to-grade folder structure mapped against a provided student roster (CSV file).

## Usage
NormLab is executed via the command line, requiring three arguments: the target root zip file, the desired output directory, and a CSV file containing the student information.

```bash
python main.py <target_zip_path> <output_path> <student_info_csv_path>
```

**Example:**
```bash
python main.py "D:\Develop\Python\NormLab\Lab03-JUnit for Unit Test.zip" "D:\Develop\Python\NormLab\Output" "D:\Develop\Python\NormLab\student_info\International Student List.csv"
```

## Software Architecture & Key Design Decisions

NormLab is built with clean architecture principles in mind, focusing on extensibility, code reusability, and separation of concerns. Below are the key design decisions:

### 1. Strategy & Template Method Patterns for File Traversal
Processing student submissions requires iterating over complex, nested directory trees. Instead of writing monolithic recursive functions, the project abstracts the traversal logic into a `TraverseTool` base class ([src/traverse_tool.py](src/traverse_tool.py)). Specific operations are implemented as modular subclasses. This applies the Strategy and Template Method patterns:
- **`UnarchiveTool`**: Identifies and recursively extracts nested `.zip` and `.rar` files.
- **`FileFilterTool`**: Cleans up ignored files, junk data, and prunes empty directories.
- **`FindDocTool`**: Locates important grading documents (`.doc`, `.docx`, `.pdf`) and standardizes document file names according to the CSV manifest.
- **`StructureFilterTool`**: Detects and flattens redundantly nested directories.

### 2. The Controller Pattern
The hierarchy of the execution process is managed using a Controller pattern to decouple the bulk archive logic from the individual student submission logic.
- **`Normlab` (Main Orchestrator)**: Acts as the top-level processor. It parses the student roster CSV, extracts the root bulk file, and initializes individual sub-controllers.
- **`LabController`**: Manages the state and transformation operations for a single student's lab submission. It securely holds the student's ID, full name, and short name, applying the renaming logic gracefully.

### 3. Pipeline Processing
The execution model in [main.py](main.py) is structured as a clear data transformation pipeline. The submissions are passed through a distinct sequence of operational layers:
`Unarchive` -> `Filter Junk` -> `Find & Rename Docs` -> `Reorganize Structure`

This pipeline approach is highly readable and extensible. If a new step is needed in the future (e.g., adding an automatic plagiarism check), developers can simply write a new `TraverseTool` and append it to the `test_normlab.execute()` pipeline.

### 4. Encapsulation of Archive Implementations
To handle different archive formats seamlessly, the project uses an `ArchiveFile` base abstraction ([src/archive_tool.py](src/archive_tool.py)). The `CustomZipFile` and `CustomRarFile` classes use multiple inheritance to extend both `ArchiveFile` and their respective underlying library implementations (`zipfile` and `rarfile`). This encapsulates format-specific quirks—such as dealing with character encoding anomalies (like `gbk` vs `utf-8` decoding in zip internals)—away from the main pipeline logic.