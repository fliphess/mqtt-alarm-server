# MQTT Alarm display - Server Component

This is the server side component of the [esp8266 mqtt alarm display](https://github.com/fliphess/esp8266_alarm_display).
It listens on a MQTT topic for authentication requests and adjusts the [home assistant manual mqtt alarm panel](https://www.home-assistant.io/components/alarm_control_panel.manual_mqtt/) accordingly.

If the UID and the passcode match a person in the yaml configuration file and this person is allowed to manage the alarm in the current timeslot,
An certain action is triggered, depending on which request was performed on the mqtt alarm display.


## Example

OK:

```
    DISPLAY: home/alarm/rfid {"hostname":"alarmdisplay1.home","uid":"12AB34","code":"1234","action":1}
    SERVER:  home/alarm/display/alarmdisplay1.home {"access": "GRANTED", "name": "Flip", "uid": "12AB34"}
    SERVER:  home/alarm/set DISARM
    HASS:    home/alarm disarmed
    SERVER:  home/alarm/display disarmed
```

NOK:

```
    DISPLAY: home/alarm/rfid {"hostname":"alarmdisplay1.home","uid":"12AB35","code":"1234","action":1}
    SERVER:  home/alarm/display/alarmdisplay1.home {"access": "DENIED", "name": "unknown", "uid": "12AB35"}
```


## Setup

### Install

Clone repo, create a virtualenv and install `mqtt_alarm_server` and its requirements:

```
    git clone https://github.com/fliphess/mqtt_alarm_server.git && cd mqtt_alarm_server
    mkvirtualenv -p "$( which python3 )" -a "$( pwd )" mqtt_alarm_server
    pip install .
```

### Configure

Copy the config file and adjust the settings

```
    cp settings.yaml.example settings.yaml && vim settings.yaml
```

## Run

Run the server:

```
    mqtt-alarm-server -c settings.yaml -vvvv
```
