from mycroft import MycroftSkill, intent_file_handler


class PatrickLightsOff(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('off.lights.patrick.intent')
    def handle_off_lights_patrick(self, message):
        self.speak_dialog('off.lights.patrick')


def create_skill():
    return PatrickLightsOff()

