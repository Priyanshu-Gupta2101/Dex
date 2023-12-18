# Dex: Hand Gesture Recognition for Online Meetings
## Deprecated needs to be updated

Dex is a system that leverages hand gesture recognition to enhance the user experience during online meetings, such as Zoom or Google Meet. With Dex, users can express reactions and interact in a more dynamic way by using hand gestures.

## Features

- **Hand Gesture Recognition**: Dex employs advanced hand gesture recognition technology to interpret users' hand movements during online meetings.
  
- **Reaction Display**: Users can use specific hand gestures to display predefined reactions, adding a new layer of expressiveness to virtual interactions.

- **Integration with OBS Virtual Studio**: Dex seamlessly integrates with OBS Virtual Studio, turning it into a virtual camera. This allows users to use Dex's hand gesture recognition as input for their virtual camera feed.

## Technology Stack

- **Python**: The backend of Dex is built using Python, leveraging the Django framework.
  
- **Django**: The web framework Django is utilized to facilitate the development of the backend, ensuring a robust and scalable solution.

- **OBS Virtual Studio**: Dex integrates with OBS Virtual Studio, transforming it into a virtual camera.

## Usage

1. **Setup**: Ensure that your system has the necessary hardware and software requirements for hand gesture recognition.

2. **Installation**:
   ```bash
   git clone https://github.com/your-username/dex.git
   cd dex
   pip install -r requirements.txt
   ```

3. **Run the Server**:
   ```bash
   python manage.py runserver
   ```

4. **Access Dex**: Open your web browser and navigate to [http://localhost:8000](http://localhost:8000).

5. **Configure Gestures**: Configure and calibrate hand gestures based on your preferences.

6. **Integration with OBS Virtual Studio**:
   - Download and install [OBS Virtual Studio](https://obsproject.com/).
   - In OBS, go to "Tools" > "VirtualCam" and start the virtual camera.

7. **Join an Online Meeting**: Start an online meeting on platforms like Zoom or Google Meet.

8. **Select Dex Virtual Camera**: In your online meeting platform, select the virtual camera provided by OBS (usually named "OBS Virtual Camera").

9. **Express Reactions**: Use predefined hand gestures to express reactions during the meeting.

## Additional Gestures

To add more gestures, consider using libraries such as Mediapipe and the Teachable Machine website for training and incorporating new gestures into Dex.

## Contributing

Contributions to Dex are encouraged! If you have ideas for improvements, additional features, or bug fixes, feel free to fork the repository, make your changes, and submit a pull request.

## Issues

If you encounter any issues or have suggestions, please report them on the [GitHub Issues](https://github.com/your-username/dex/issues) page.

## License

Dex is licensed under the [MIT License](LICENSE).
