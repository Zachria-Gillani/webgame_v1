class Room(object):

     def __init__(self, name, description):
         self.name = name
         self.description = description
         self.paths = {}

     def go(self, direction):
         return self.paths.get(direction, None)

     def add_paths(self, paths):
         self.paths.update(paths)


vault = Room("Vault",
"""
The Brotherhood has attacked the Castle, the main base of the
Hourmen.  You are the Commander of the Hourmen.
They have overun Castle.
As commander, you know what you must
fight to the fusion core room, take the core
put the core in the gangway, blow up the gangway,
run to the airship.

You hoof it to the fusion core room, passing the vault room.
Just then, a Brother Bot jumps out and pulls a gun on you.
""")

fusion_core_room = Room("Fusion Core Room",

"""
You are lucky enough to have brought your lucky plasma blaster and lucky dance.
You use the rehearsed moves that allow you to weave through a series of blasts.
Your lucky dance ends with throwing the plasma grenade at the Brother Bot.
You take cover as the Bot explodes.
You continue on to the fusion core room.

You bust open the doors to the fusion core room.
Three surpised Brother Bots are caught off guard.
You quickly dispose of them by cutting their processors.
Now you walk to the fusion core.
You had made a passcode so only you could take it out.
The code is 3 letters.
""")


gangway = Room("Gangway",
"""
The acceptance key beeps.  The core comes out of place.
You grab the core and make your way to the gangway.

As you open the door to the gangway, you see 2 Mega Brother Bots.
They stand 20 feet in height like Mechs.
""")


airship = Room("Airship",
"""
You stop and think to yourself, it is now or never.
You activate the button on your mechanical chest.
Your body errupts in a mechanical robot suit.
You have programmed an AI that learns from machine patterns.
It asks for your command.  You script a command quickly via
nattural language command.
The suit jolts forward, diving past gunfire with great agility.
Before you know it, your suit automatically deactivates the program.
You see the 2 mechs destroyed in flames.
You are in the airship.
You have made a last natural language command interface with the airship.
What was the phrase?
""")

finish_win = Room("Fin",
"""
You final stutter out the passphrase.  The airship clicks on and welcomes you.
The airships sensors sense the fusion core is about to explode.
The AI in the ship immediately turns on and starts to fly away.
You go to a window and see the gangway explode trapping the Brother Bots insdie.
You have survived.
""")

finish_lose = Room("Fin",
"""
You say the wrong code, too bad.  The fusion core explodes.
"""
)

airship.add_paths({
'2':finish_win,
'*':finish_lose
})

sad_death = Room("death", "You have died, your cause is lost.")

gangway.add_paths({
'throw the core':sad_death,
'activate suit':airship
})

fusion_core_room.add_paths({
'admin'
'*':sad_death
})

vault.add_paths({
'shoot':sad_death,
'lucky dance':fusion_core_room,
'run':sad_death
})

START = 'vault'

def load_room(name):
    """
    Something seems to mayhaps be astray here.
    Who is the name of the player?
    """
    return globals().get(name)

def name_room(room):
    """
    Who is this room?
    Deceitful room!
    Let us make it global
    """

    for key, value in globals().items():
        if value ==room:
            return key
