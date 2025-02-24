# Static Site Generator

A static site generator that transforms Markdown files into a static HTML website.

## Features

- Converts Markdown files to HTML
- Supports nested directory structures
- Custom HTML templating
- Code block syntax highlighting
- Image handling
- Smart link processing
- Blockquote formatting
- Lists (ordered and unordered)

## Installation

```bash
# Clone the repository
git clone https://github.com/JansenMitchell/static_site_generator
cd static_site_generator

# Ensure you have Python 3.x installed
python3 --version
```

## Usage

```bash
# Run the generator and start local server
sh main.sh

# Run the test suite
sh test.sh
```

## Project Structure

```
.
├── content/           # Source Markdown files
├── public/           # Generated HTML output
├── src/             # Python source code
├── static/          # Static assets (CSS, images)
├── template.html    # HTML template
├── main.sh         # Build script
└── test.sh         # Test runner
```

## How It Works

1. `markdowntohtml.py` converts Markdown to HTML nodes
2. `generate_page.py` processes files and applies templates  
3. `splitnodes.py` handles text parsing and node creation

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/name`)
3. Make your changes
4. Run tests (`sh test.sh`)
5. Commit changes (`git commit -am 'Add feature'`)
6. Push to branch (`git push origin feature/name`)
7. Create Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Tests

Run the test suite:

```bash
sh test.sh
```

Test files are located in `src/` with the `test_` prefix.