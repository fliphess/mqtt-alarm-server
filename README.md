# MQTT Alarm display - Server Component

This is the server side component of the [esp8266 mqtt alarm display](https://github.com/fliphess/esp8266_alarm_display).
It listens on a MQTT topic for authentication requests and adjusts the [home assistant manual mqtt alarm panel](https://www.home-assistant.io/components/alarm_control_panel.manual_mqtt/) accordingly.

If the UID and the passcode match a person in the yaml configuration file and this person is allowed to manage the alarm in the current timeslot,
An action will be performed, depending on which request was performed on the mqtt alarm display.


## Flow

1. A token is passed or an alarm code is entered on the display.
2. The display sends the uuid of the token, the passcode and the requested action as a json to the `rfid_auth_topic` mqtt topic.
3. The mqtt alarm server checks the uuid and the passcode in it's configuration.
4. A status message is send to the topic the display is listening on (`display_topic/$HOSTNAME`).
5. The server sends an mqtt update to the homeassistant alarm command topic to change the alarm state.
6. Home assistant changes the alarm state and sends an update to the `state_topic`.
7. The server proxies this alarm state to the `display_topic`.
8. The display updates the display panel to the current alarm state and waits for new input.


## Setup

### Install

Clone repo, create a virtualenv and install `mqtt_alarm_server` and its requirements

```
  git clone https://github.com/fliphess/mqtt_alarm_server.git && cd mqtt_alarm_server
  mkvirtualenv -p "$( which python3 )" -a "$( pwd )" mqtt_alarm_server
  pip install -r requirements.txt
```

### Configure

Copy the config file and adjust the settings

```
  cp settings.yaml.example settings.yaml && vim settings.yaml
```

## Run

Run the server:

```
./alarm-server.py -c settings.yaml -vvvv
```
