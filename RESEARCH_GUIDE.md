# Research Organization Guide

This repository is organized to help you manage research materials effectively.

## Folder Structure

### 📚 `/books/`
Store full books, book chapters, or lengthy texts here.
- Organize by author or topic if you have many
- Example: `books/AuthorName_BookTitle.pdf`

### 📄 `/articles/`
Research papers, journal articles, and academic publications.
- Consider subfolders by topic or year
- Example: `articles/machine-learning/paper-name.pdf`

### 📝 `/notes/`
Your personal notes, summaries, and annotations.
- Create markdown files with your insights
- Example: `notes/book-summary-title.md`

### 🔖 `/references/`
Bibliographies, citation lists, and reference materials.
- Keep BibTeX files, citation exports here
- Example: `references/ml-papers.bib`

### 🔬 `/projects/`
Organized research projects by topic.
Each project can have its own subfolder with:
- Related articles
- Notes
- Analysis
- Code/scripts

Example structure:
```
projects/
└── topic-name/
    ├── articles/
    ├── notes.md
    └── analysis/
```

## Quick Start

### Adding Files

1. **PDFs and Documents**: Just drag and drop into the appropriate folder
2. **Notes**: Create `.md` (markdown) files for easy reading on GitHub

### Using Git

```bash
# Add all new files
git add .

# Commit with a descriptive message
git commit -m "Add research articles on [topic]"

# Push to GitHub
git push -u origin claude/github-research-analysis-setup-01S7rb1PV6S9W3Dh9S6P4y6L
```

## Tips

- Use clear, descriptive file names
- Add a README.md in each folder to describe contents
- Keep large files (<100MB) or use Git LFS for very large files
- Use markdown (.md) for notes - it's readable on GitHub

## Searching Your Research

GitHub's search works great for text files and markdown.
For PDFs, keep companion `.md` files with summaries and key points.
