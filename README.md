Typing Practice Game

A simple typing game built in Python designed to help users improve their typing speed and accuracy. 
The application reads a text file, displays the content, and allows the user to type along with visual feedback.

===================
Features
===================

- Launches with a main window and opens a folder dialog to select a text file
- Loads the selected text into the interface
- Highlights the current character to type in yellow
- Correct keystrokes turn green
- Incorrect keystrokes turn red
- Displays real-time typing statistics in the top-left corner:
  - Characters per second (CPS)
  - Words per second (WPS)
- Automatically pauses stats and progression when:
  - The text ends
  - Enter key is pressed again
  - Mouse leaves the typing window
- Resumes typing only when:
  - The window is re-selected
  - Enter key is pressed again
  - Statistics reset upon resume

===================
How to Use
===================

1. Run the Python script:
   python typing_game.py

2. The main game window will open. A file dialog will prompt you to select a .txt file to use as the typing material.

3. Once the file is selected:
   - Press Enter to begin typing.
   - Type the text shown on the screen.
   - Watch the CPS and WPS statistics update in real-time.

4. Pause the session by:
   - Pressing Enter
   - Moving the mouse out of the window

5. Resume typing by clicking the window and pressing Enter. Stats will reset.

===================
Requirements
===================

- Python 3.6+
- Libraries:
  - tkinter (standard)
  - time (standard)
  - os (standard)

===================
Future Improvements
===================

- Add a countdown before starting
- Support paragraph-based progression
- Enable custom fonts and color themes
- Add accuracy percentage

===================
License
===================

This project is licensed under the MIT License.
You are free to use, modify, and distribute it with proper attribution.
