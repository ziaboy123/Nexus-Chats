# Nexus-Chats

This is my A-level Computer Science Coursework. It has three main features. A direct messaging chat, an anonymous chat and a chat forum. (I have been trying to figure out a shorter way to run this).
<p>
Nexus has three different varieties of messaging systems for users to communicate in.
‘The Link Network’ which is a direct messaging system where users can speak directly to whoever they wish. ‘The Phantom Zone’ which is an anonymous chatting system where users can assign themselves a temporary name and generate a room to talk to anyone that they share their room code with. Each room as well as its contents gets deleted as soon as it contains no users. ‘Interspace’ is a chatting system where users can join a space from the list of available options and speak to whomever you wish about the topic associated with that space. Unlike ‘The Phantom Zone’, messages are always kept regardless of how many people are in a certain space. 
</p>

**Dependencies:**
* **JS Stuff:** On Visual Studio Code, first click on any of the files in client or server and then at the bottom of the 'explorer' tab you should see a tab called 'NPM Scripts'. On this tab there will be three files in each section called install. Click on these one at a time and wait for some dependancies to install.
* **Python Stuff:** On Visual Studio Code, cd into 'other-chats' and in the integrated terminal do 'pip install Flask' and 'pip install flask-socketio'.
* **NodeJS Stuff:** cd into 'client', 'server' and 'socket' and do 'npm install'.

**To run:** _(Do these in terminal and open a new terminal every two bullet points)_
* cd client
* npm run dev
* cd other-chats
* python app.py
* cd other-chats
* python main.py
* cd server
* nodemon
* cd socket
* nodemon
