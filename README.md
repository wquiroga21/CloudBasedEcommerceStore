# Overview

In this project, I have developed an e-commerce platform designed to streamline online shopping and product management. This software allows users to browse products, manage their shopping cart, and process orders through a user-friendly interface. To support scalability and real-time data synchronization, the platform integrates with Google's Firestore, a cloud-based database.

The purpose behind creating this software was to deepen my understanding of cloud databases and to explore the practical aspects of developing a full-stack application with a focus on backend services. This project enabled me to gain hands-on experience with Firestore, enhancing my skills in database management, API integration, and server-side logic.


# Cloud Database

For this project, I utilized Google Firestore, a flexible, scalable database for mobile, web, and server development from Firebase and Google Cloud Platform. Firestore provides powerful querying, real-time updates, and multi-region data replication which is crucial for building responsive e-commerce platforms.

The database structure includes three main collections: `Products`, `Users`, and `Orders`. The `Products` collection stores details about the items for sale, including name, description, price, and stock quantity. The `Users` collection manages user authentication and profile information. The `Orders` collection tracks user orders, including product IDs, quantities, and order status.

# Development Environment

The primary tools and technologies used in the development of this software include:

- **Visual Studio Code**: as the Integrated Development Environment (IDE).
- **Python**: the main programming language for backend development.
- **Firebase Admin SDK**: a set of server libraries that allows interacting with Firebase from privileged environments to manage users, manipulate Firestore databases, and more.
- **Git**: for uploading updated versions.

# Useful Websites

Below are some of the websites that were invaluable in completing this project:

- [Firebase Documentation](https://firebase.google.com/docs)
- [Python Firestore](https://googleapis.dev/python/firestore/latest/index.html)
- [Stack Overflow](http://stackoverflow.com)

# Future Work

There are several areas of improvement and additional features I plan to implement:

- **User Interface Enhancements**: To improve the user experience by implementing a more intuitive and responsive design.
- **Advanced Product Search**: Incorporating advanced search capabilities to help users find products more efficiently.
- **Payment Integration**: Adding support for processing payments to complete the shopping experience.
