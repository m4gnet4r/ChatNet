# ChatNet
A secure TCP-based encrypted chat platform that allows users to communicate in a networked environment. ChatNet uses RSA encryption to ensure messages are secure and provides both broadcast and private messaging functionality.

## Features

- **Secure Communication**: All messages are encrypted using RSA public/private key pairs
- **User Authentication**: Each client connects using a nickname
- **Multiple Chat Modes**:
  - Broadcast messages to all connected clients
  - Direct messaging to specific users
  - List all connected users
- **Real-time Communication**: Implemented using threading for simultaneous sending and receiving
- **Graceful Disconnection**: Proper handling of client disconnection

## Requirements

- Python 3.13+
- rsa library
- socket library (built-in)
- threading library (built-in)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/m4gnet4r/ChatNet.git
   cd ChatNet
   ```

2. Install the required dependencies:
   ```bash
   pip install rsa
   ```

## Usage

### Step 1: Generate Key Pairs

Before starting the server or client, you need to generate RSA key pairs. This only needs to be done once:

```bash
python key_generator.py
```

This will create two files in the current directory:
- `public.pem`: The public key used for encryption
- `private.pem`: The private key used for decryption

### Step 2: Start the Server

Start the chat server:

```bash
python server.py
```

You should see the message "server is listening..." indicating the server is running and waiting for connections.

### Step 3: Connect Clients

Start one or more clients in separate terminal windows:

```bash
python client.py
```

When prompted, enter a unique nickname for the client.

## Commands

Once connected, you can use the following commands in the chat:

- **Broadcast Message**: Just type your message and press enter to send to all connected clients
- **Direct Message**: Type `dm` and press enter. Then follow the prompts:
  - Enter recipient nicknames separated by commas
  - Enter your message
- **List Users**: Type `list` to see all connected users
- **Quit**: Type `quit` to disconnect from the chat

## Testing

To test the application:

1. Open three terminal windows
2. In the first window, run the server:
   ```bash
   python server.py
   ```
3. In the second window, run a client and choose a nickname (e.g., "Joy"):
   ```bash
   python client.py
   ```
4. In the third window, run another client and choose a different nickname (e.g., "Rohan"):
   ```bash
   python client.py
   ```
5. Test the different chat functionalities using the commands as given in [command section](https://github.com/m4gnet4r/ChatNet?tab=readme-ov-file#commands)
   
## Architecture

- **Server (`server.py`)**: Handles multiple client connections, message broadcasting, and direct messaging
- **Client (`client.py`)**: Connects to server, sends/receives messages, handles encryption/decryption
- **Key Generator (`key_generator.py`)**: Creates the RSA key pair for secure communication

## Limitations

- Currently configured for local use (localhost)
- For remote connections, modify the host IP in both server and client files
- The message size is limited due to RSA encryption constraints

## Contact

For questions or support, please contact [GitHub: m4gnet4r](https://github.com/m4gnet4r)
