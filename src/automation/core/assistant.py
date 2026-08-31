from __future__ import annotations

from automation.commands.command_parser import CommandParser
from automation.commands.command_matcher import CommandMatcher
from automation.commands.command_mapper import CommandMapper
from automation.devices.actions.linux.linux_action_suite import (LinuxActionSuite,)
from automation.voice.voice_output import VoiceOutput

class Assistant:

    def __init__(self):
        self.parser = CommandParser()
        self.matcher = CommandMatcher()
        self.mapper = CommandMapper()
        self.actions = LinuxActionSuite()
        self.voice = VoiceOutput()

    def handle(self,text: str,):
        print("\nUSER :", text)
        tokens = self.parser.tokenize(text)
        action = self.matcher.match(tokens)
        if not action:
            msg = "Sorry, I did not understand"
            print("❌", msg)
            self.voice.speak(msg)
            return None
        request = self.mapper.map(action, tokens)
        if not request:
            msg = "Failed to process command"
            print("❌", msg)
            self.voice.speak(msg)
            return None
        result = self.actions.registry.execute(request)
        msg = f"Done {request.action}"
        print("✅ Result :", result)
        self.voice.speak(msg)
        return result

    def __repr__(self):
        return "<Assistant>"
