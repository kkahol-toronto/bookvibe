# BookVibe - AI-Powered Library Management System

A modern, AI-powered library management system built with FastAPI and Python. BookVibe provides comprehensive book management capabilities with intelligent description generation tailored to different audiences.

## 🚀 Features

### Core Features
- **Book Management**: Add, edit, and delete books with comprehensive metadata
- **Check-in/Check-out System**: Track book borrowing with borrower information
- **Advanced Search**: Search books by title, author, ISBN, or genre
- **Real-time Statistics**: Dashboard with library statistics and insights

### AI-Powered Features
- **Smart Description Generation**: Generate compelling book descriptions using Azure OpenAI
- **Audience Targeting**: Tailor descriptions for different demographics:
  - **Gen Z** (Ages 9-24): Digital natives who value authenticity and social justice
  - **Millennials** (Ages 25-40): Tech-savvy adults who appreciate meaningful experiences
  - **Gen X** (Ages 41-56): Independent, resourceful adults who value practicality
  - **Baby Boomers** (Ages 57-75): Traditional values, prefer detailed information
  - **Silent Generation** (Ages 76+): Respectful of tradition, value clear communication

### User Experience
- **Modern UI**: Beautiful, responsive design with Bootstrap 5
- **Real-time Updates**: Instant feedback and dynamic content
- **Mobile-Friendly**: Optimized for all device sizes
- **Intuitive Navigation**: Easy-to-use interface with clear workflows

## 🛠️ Technology Stack

- **Backend**: FastAPI (Python)
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **AI Integration**: Azure OpenAI GPT models
- **Templating**: Jinja2
- **Styling**: Custom CSS with modern gradients and animations

## 📋 Prerequisites

- Python 3.8 or higher
- Azure OpenAI API access (for AI features)

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd LibraryManagementSystem
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   AZURE_OPENAI_ENDPOINT=your_azure_openai_endpoint
   AZURE_OPENAI_KEY=your_azure_openai_api_key
   AZURE_OPENAI_DEPLOYMENT=your_deployment_name
   ```

5. **Run the application**
   ```bash
   python main.py
   ```

6. **Access the application**
   Open your browser and navigate to `http://localhost:8000`

## 🚀 Quick Start

1. **Add Your First Book**
   - Click "Add New Book" from the dashboard
   - Fill in the required information (title, author, ISBN, genre, year)
   - Optionally add a description

2. **Generate AI Descriptions**
   - Navigate to "AI Descriptions" in the menu
   - Select a book and target audience
   - Click "Generate Description" to create tailored content

3. **Manage Checkouts**
   - Use the "Check Out" button to borrow books
   - Enter borrower information
   - Use "Check In" to return books

4. **Search Your Collection**
   - Use the search functionality to find specific books
   - Filter by title, author, ISBN, or genre

## 📊 Database Schema

The application uses SQLite with the following main table:

```sql
CREATE TABLE books (
    id INTEGER PRIMARY KEY,
    title VARCHAR NOT NULL,
    author VARCHAR NOT NULL,
    isbn VARCHAR UNIQUE NOT NULL,
    genre VARCHAR NOT NULL,
    publication_year INTEGER NOT NULL,
    description TEXT,
    is_checked_out BOOLEAN DEFAULT FALSE,
    checked_out_by VARCHAR,
    checked_out_date DATETIME,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

## 🔌 API Endpoints

- `GET /` - Main dashboard
- `GET /add-book` - Add book form
- `POST /add-book` - Create new book
- `GET /edit-book/{id}` - Edit book form
- `POST /edit-book/{id}` - Update book
- `POST /delete-book/{id}` - Delete book
- `POST /checkout/{id}` - Check out book
- `POST /checkin/{id}` - Check in book
- `GET /search` - Search books
- `GET /generate-descriptions` - AI description generator
- `POST /generate-description` - Generate AI description
- `GET /api/books` - JSON API for books

## 🎨 Customization

### Styling
The application uses custom CSS variables for easy theming:
```css
:root {
    --primary-color: #2c3e50;
    --secondary-color: #3498db;
    --accent-color: #e74c3c;
    --success-color: #27ae60;
    --warning-color: #f39c12;
}
```

### Adding New Genres
Edit the genre options in `templates/add_book.html` and `templates/edit_book.html`.

## 🚀 Deployment

### Local Development
```bash
python main.py
```

### Production Deployment
1. Set up a production server (e.g., Ubuntu with Nginx)
2. Install Python and dependencies
3. Configure environment variables
4. Use a process manager like systemd or supervisor
5. Set up reverse proxy with Nginx

### Docker Deployment (Optional)
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "main.py"]
```

## 🔒 Security Considerations

- Store API keys securely in environment variables
- Implement proper authentication for production use
- Use HTTPS in production
- Regular database backups
- Input validation and sanitization

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is open source and available under the MIT License.

## 🆘 Support

For issues and questions:
1. Check the documentation
2. Review existing issues
3. Create a new issue with detailed information

## 🎯 Future Enhancements

- User authentication and roles
- Advanced reporting and analytics
- Book cover image upload
- Email notifications for due dates
- Integration with external book APIs
- Mobile app development
- Multi-language support

---

**Built with ❤️ using FastAPI and Azure OpenAI** 