<!DOCTYPE html>
<html lang="en">
<body>

<h1>📦 AVANT Inventory Management System</h1>
<p>
  A Python-based inventory management system with a graphical interface using Tkinter. This project provides functionalities like adding, updating, removing, and viewing inventory details.
</p>

<h2>🌟 Key Features</h2>
<ul>
  <li>📋 Add, update, and delete inventory items.</li>
  <li>📊 Real-time inventory storage tracking with visual progress indicators.</li>
  <li>🔍 Search and browse inventory items by ID.</li>
  <li>👨‍💼 Employee management with pre-defined roles and login credentials.</li>
  <li>🕒 Tracks the last updated date and time for inventory items.</li>
</ul>

<h2>⚙️ Technology Stack</h2>
<ul>
  <li><strong>Programming Language:</strong> Python</li>
  <li><strong>Database:</strong> MySQL</li>
  <li><strong>Libraries/Frameworks:</strong> Tkinter, PIL, MySQL Connector</li>
</ul>

<h2>🚀 Setup & Installation</h2>
<ol>
  <li>Install Python 3.x from the official <a href="https://www.python.org/downloads/">Python website</a>.</li>
  <li>Install MySQL and set up the database with the credentials:
    <ul>
      <li>Host: localhost</li>
      <li>User: root</li>
      <li>Password: 12345</li>
    </ul>
  </li>
  <li>Run the script to create the database and tables automatically:
    <div class="code-block">python inventory_management.py</div>
  </li>
  <li>Install the required Python libraries:
    <div class="code-block">pip install mysql-connector-python pillow</div>
  </li>
</ol>

<h2>📚 Functionalities</h2>
<ul>
  <li>🏷️ <strong>Add Item:</strong> Add new products to the inventory by specifying their ID, name, and quantity.</li>
  <li>🔄 <strong>Update Item:</strong> Update the quantity of existing items in the inventory.</li>
  <li>🗑️ <strong>Remove Item:</strong> Delete an item from the inventory by ID.</li>
  <li>🔍 <strong>Search Item:</strong> Browse and view details of a specific inventory item.</li>
  <li>📦 <strong>Storage Indicator:</strong> Visual progress bar to monitor storage capacity.</li>
</ul>

<h2>🧑‍💻 Predefined Employee Roles</h2>
<p>Below are the predefined employees added to the system with roles and credentials:</p>
<table>
  <thead>
    <tr>
      <th>Employee No</th>
      <th>Name</th>
      <th>Position</th>
      <th>Salary</th>
      <th>Email</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>526485</td>
      <td>Nikhil Anto</td>
      <td>Inventory Manager</td>
      <td>$6500</td>
      <td>nikhil1975@gmail.com</td>
    </tr>
    <tr>
      <td>856936</td>
      <td>Subash Nair</td>
      <td>Inventory Specialist</td>
      <td>$6333</td>
      <td>1983subash@gmail.com</td>
    </tr>
  </tbody>
</table>

<h2>💡 Fun Fact</h2>
<p>
  This project started as an idea to streamline warehouse operations for small businesses, providing a simple yet powerful interface for inventory management.
</p>

<h2>✨ Quote</h2>
<blockquote>
  "Inventory is money sitting around in another form." - Rhonda Abrams
</blockquote>

</body>
</html>
