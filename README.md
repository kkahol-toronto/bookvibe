# BookVibe - AI-Powered Library Management System

<div align="center">

![BookVibe Logo](docs/images/bookvibe-logo.png)

**A modern, AI-powered library management system built with FastAPI and Python**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen.svg)]()

*Transform your library management with AI-powered book descriptions tailored to different audiences*

</div>

## 📖 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Screenshots](#-screenshots)
- [Technology Stack](#-technology-stack)
- [Quick Start](#-quick-start)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [API Documentation](#-api-documentation)
- [Database Schema](#-database-schema)
- [Deployment](#-deployment)
- [Contributing](#-contributing)
- [License](#-license)

## 🎯 Overview

BookVibe is a comprehensive library management system that combines traditional book management features with cutting-edge AI technology. Built with FastAPI and Python, it provides an intuitive interface for managing book collections while leveraging Azure OpenAI to generate compelling book descriptions tailored to different audience demographics.

### Key Highlights

- **🤖 AI-Powered Descriptions**: Generate engaging book descriptions for different audiences (Gen Z, Millennials, Gen X, Baby Boomers, Silent Generation)
- **📱 Modern UI**: Beautiful, responsive design that works on all devices
- **⚡ Fast Performance**: Built with FastAPI for high-performance web applications
- **🔍 Advanced Search**: Powerful search functionality across all book metadata
- **📊 Real-time Statistics**: Live dashboard with library insights
- **🔄 Check-in/Check-out System**: Complete borrowing management

## ✨ Features

### Core Library Management
- **📚 Book Management**: Add, edit, and delete books with comprehensive metadata
- **🔍 Advanced Search**: Search by title, author, ISBN, or genre with real-time filtering
- **📋 Check-in/Check-out**: Track book borrowing with borrower information and timestamps
- **📊 Dashboard Analytics**: Real-time statistics and library insights
- **📱 Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices

### AI-Powered Features
- **🎯 Audience-Targeted Descriptions**: Generate descriptions for specific demographics:
  - **Gen Z (Ages 9-24)**: Digital natives who value authenticity and social justice
  - **Millennials (Ages 25-40)**: Tech-savvy adults who appreciate meaningful experiences
  - **Gen X (Ages 41-56)**: Independent, resourceful adults who value practicality
  - **Baby Boomers (Ages 57-75)**: Traditional values, prefer detailed information
  - **Silent Generation (Ages 76+)**: Respectful of tradition, value clear communication
- **🔄 Multiple Descriptions**: Store and display descriptions for all audiences
- **📈 Description History**: Track when descriptions were generated
- **🎨 Visual Organization**: Color-coded descriptions by audience type

### User Experience
- **🎨 Modern Interface**: Clean, intuitive design with smooth animations
- **⚡ Real-time Updates**: Instant feedback and dynamic content
- **🔧 Easy Management**: Streamlined workflows for common tasks
- **📖 Detailed Book Views**: Comprehensive information pages for each book

## 📸 Screenshots

<div align="center">

### Main Dashboard
![Main Page](docs/images/main_page.png)
*Comprehensive library overview with statistics and book collection*

### Book Details Page
![Book Information](docs/images/book_info.png)
*Detailed view showing all book information and AI-generated descriptions*

### Add Book Form
![Add Book](docs/images/add_book.png)
*Intuitive form for adding new books to the collection*

### Search Interface
![Search Page](docs/images/search_page.png)
*Advanced search functionality with real-time filtering*

### AI Description Generator
![AI Generator](docs/images/ai_generator.png)
*Generate tailored descriptions for different audience demographics*

</div>

## 🛠️ Technology Stack

### Backend
- **FastAPI** - Modern, fast web framework for building APIs
- **SQLAlchemy** - SQL toolkit and Object-Relational Mapping (ORM)
- **SQLite** - Lightweight, serverless database
- **Pydantic** - Data validation using Python type annotations

### Frontend
- **HTML5/CSS3** - Modern web standards
- **Bootstrap 5** - Responsive CSS framework
- **JavaScript** - Interactive functionality
- **Font Awesome** - Icon library

### AI Integration
- **Azure OpenAI** - GPT models for description generation
- **OpenAI Python SDK** - Official Python client

### Development Tools
- **Python 3.8+** - Programming language
- **Uvicorn** - ASGI server for FastAPI
- **Jinja2** - Template engine
- **python-dotenv** - Environment variable management

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Azure OpenAI API access (for AI features)

### 1. Clone the Repository
```bash
git clone https://github.com/kkahol-toronto/bookvibe.git
cd bookvibe
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment
```bash
cp env.example .env
# Edit .env with your Azure OpenAI credentials
```

### 5. Run the Application
```bash
python main.py
```

### 6. Access BookVibe
Open your browser and navigate to `http://localhost:8000`

## 📋 Installation

### Detailed Setup Instructions

1. **System Requirements**
   - Python 3.8 or higher
   - 4GB RAM minimum
   - 1GB free disk space

2. **Dependencies Installation**
   ```bash
   # Install system dependencies (Ubuntu/Debian)
   sudo apt-get update
   sudo apt-get install python3-pip python3-venv
   
   # Install Python dependencies
   pip install -r requirements.txt
   ```

3. **Database Setup**
   ```bash
   # The database will be created automatically on first run
   # To populate with sample data:
   python sample_data.py
   ```

4. **Environment Configuration**
   Create a `.env` file in the root directory:
   ```env
   # Azure OpenAI Configuration
   AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
   AZURE_OPENAI_KEY=your_azure_openai_api_key_here
   AZURE_OPENAI_DEPLOYMENT=your_deployment_name_here
   
   # Optional: Server Configuration
   HOST=0.0.0.0
   PORT=8000
   DEBUG=True
   ```

## ⚙️ Configuration

### Azure OpenAI Setup

1. **Create Azure OpenAI Resource**
   - Go to Azure Portal
   - Create a new Azure OpenAI resource
   - Note your endpoint URL and API key

2. **Deploy GPT Model**
   - In your Azure OpenAI resource, deploy a GPT model
   - Note the deployment name

3. **Configure Environment Variables**
   ```env
   AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
   AZURE_OPENAI_KEY=your_api_key
   AZURE_OPENAI_DEPLOYMENT=your_deployment_name
   ```

### Customization Options

- **Database**: Change `SQLALCHEMY_DATABASE_URL` in `main.py` for different databases
- **Port**: Modify the port in `main.py` or set `PORT` environment variable
- **Styling**: Customize CSS variables in `templates/base.html`

## 📖 Usage

### Getting Started

1. **Add Your First Book**
   - Click "Add New Book" from the dashboard
   - Fill in required information (title, author, ISBN, genre, year)
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

### Advanced Features

- **View Book Details**: Click "View" on any book to see comprehensive information
- **Multiple Descriptions**: Generate descriptions for all audience types
- **Real-time Statistics**: Monitor library usage and trends
- **Bulk Operations**: Manage multiple books efficiently

## 🔌 API Documentation

### REST API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Main dashboard |
| `GET` | `/add-book` | Add book form |
| `POST` | `/add-book` | Create new book |
| `GET` | `/book/{id}` | View book details |
| `GET` | `/edit-book/{id}` | Edit book form |
| `POST` | `/edit-book/{id}` | Update book |
| `POST` | `/delete-book/{id}` | Delete book |
| `POST` | `/checkout/{id}` | Check out book |
| `POST` | `/checkin/{id}` | Check in book |
| `GET` | `/search` | Search books |
| `GET` | `/generate-descriptions` | AI description generator |
| `POST` | `/generate-description` | Generate AI description |
| `GET` | `/api/books` | JSON API for books |
| `GET` | `/api/book/{id}/descriptions` | Get all descriptions for a book |

### Example API Usage

```bash
# Get all books
curl http://localhost:8000/api/books

# Get book details
curl http://localhost:8000/api/book/1/descriptions

# Generate AI description
curl -X POST http://localhost:8000/generate-description \
  -F "book_id=1" \
  -F "audience=genz"
```

## 📊 Database Schema

### Books Table

```sql
CREATE TABLE books (
    id INTEGER PRIMARY KEY,
    title VARCHAR NOT NULL,
    author VARCHAR NOT NULL,
    isbn VARCHAR UNIQUE NOT NULL,
    genre VARCHAR NOT NULL,
    publication_year INTEGER NOT NULL,
    description TEXT,
    description_audience VARCHAR,  -- Stores which audience the description targets
    is_checked_out BOOLEAN DEFAULT FALSE,
    checked_out_by VARCHAR,
    checked_out_date DATETIME,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

### Key Features

- **Audience Tracking**: `description_audience` field tracks which demographic each description targets
- **Checkout History**: Complete borrowing records with timestamps
- **Audit Trail**: Creation and update timestamps for all records

## 🚀 Deployment

### Local Development
```bash
python main.py
```

### Production Deployment

#### Option 1: Traditional Server
1. **Set up production server** (Ubuntu with Nginx)
2. **Install Python and dependencies**
3. **Configure environment variables**
4. **Use process manager** (systemd or supervisor)
5. **Set up reverse proxy** with Nginx

#### Option 2: Docker Deployment
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "main.py"]
```

#### Option 3: Cloud Platforms
- **Heroku**: Use Procfile and requirements.txt
- **Railway**: Direct deployment from GitHub
- **Render**: Free tier available for small projects
- **Vercel**: Serverless deployment option

### Environment Variables for Production

```env
# Required
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_KEY=your_production_api_key
AZURE_OPENAI_DEPLOYMENT=your_deployment_name

# Optional
DATABASE_URL=postgresql://user:pass@localhost/bookvibe
HOST=0.0.0.0
PORT=8000
DEBUG=False
```

## 🔒 Security Considerations

- **API Key Protection**: Store Azure OpenAI keys securely in environment variables
- **Input Validation**: All user inputs are validated and sanitized
- **HTTPS**: Use HTTPS in production for secure data transmission
- **Database Security**: Regular backups and access controls
- **Authentication**: Consider adding user authentication for production use

## 🤝 Contributing

We welcome contributions to BookVibe! Here's how you can help:

### Development Setup
1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make your changes**
4. **Test thoroughly**
5. **Submit a pull request**

### Contribution Guidelines
- Follow PEP 8 style guidelines
- Add tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting

### Areas for Contribution
- **Frontend Enhancements**: UI/UX improvements
- **Backend Features**: New API endpoints
- **AI Integration**: Enhanced description generation
- **Documentation**: Better guides and examples
- **Testing**: Unit and integration tests

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

### Getting Help
- **Documentation**: Check this README and inline code comments
- **Issues**: Create a GitHub issue for bugs or feature requests
- **Discussions**: Use GitHub Discussions for questions and ideas

### Common Issues
- **Port already in use**: Change the port in `main.py` or kill existing processes
- **Azure OpenAI errors**: Verify your API credentials and deployment name
- **Database issues**: Delete `library.db` to reset the database

## 🎯 Roadmap

### Planned Features
- [ ] User authentication and roles
- [ ] Advanced reporting and analytics
- [ ] Book cover image upload
- [ ] Email notifications for due dates
- [ ] Integration with external book APIs
- [ ] Mobile app development
- [ ] Multi-language support
- [ ] Advanced search filters
- [ ] Book recommendations
- [ ] Social features (reviews, ratings)

### Version History
- **v1.0.0** - Initial release with core features and AI integration
- **v1.1.0** - Enhanced UI and book details page
- **v1.2.0** - Multiple audience descriptions and improved UX

---

<div align="center">

**Built with ❤️ using FastAPI and Azure OpenAI**

[![GitHub](https://img.shields.io/badge/GitHub-View%20on%20GitHub-black.svg)](https://github.com/kkahol-toronto/bookvibe)
[![Issues](https://img.shields.io/badge/Issues-Report%20Bug-red.svg)](https://github.com/kkahol-toronto/bookvibe/issues)
[![Stars](https://img.shields.io/badge/Stars-Give%20a%20Star-yellow.svg)](https://github.com/kkahol-toronto/bookvibe/stargazers)

</div> 