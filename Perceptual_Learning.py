#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on november 21, 2022, at 09:11
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'Perceptual_Learning'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\neurolab\\Desktop\\Perceptual Learning\\Perceptual_Learning.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1280, 720], fullscr=True, screen=1, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "Welcome" ---
# Run 'Begin Experiment' code from code_2
from psychopy.hardware import keyboard #allows us to watch for key lifts 
from psychopy import event, core, visual # for when the key is first pressed
import numpy as np

import serial #Import the serial library
port = serial.Serial('COM3', baudrate = 115200) #Change 'COM3' here to your serial port address

kb = keyboard.Keyboard(bufferSize=10, waitForStart=True) #specify the keyboard object

count = 0 #might be useful to check how many trials are running

method_1 = [] #for RT data
method_2 = [] #for RT data
method_x = [] #to mark time stamp when key was lifted

key_up = [] #this will be 1 for yes and 0 for no as a condition for stimuli and triggers - reflects space bar lift
key_down = [] #same but for press down used to time the appearance of stimuli
welcome_screen = visual.ImageStim(
    win=win,
    name='welcome_screen', 
    image="welcome.png", mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=[1.8, 1],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
intr_resp = keyboard.Keyboard()

# --- Initialize components for Routine "Instr_1" ---
instr_1_screen = visual.ImageStim(
    win=win,
    name='instr_1_screen', 
    image="instr_1.png", mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=[1.8, 1],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
instr_resp_1 = keyboard.Keyboard()

# --- Initialize components for Routine "Instr_2" ---
instr_2_screen = visual.ImageStim(
    win=win,
    name='instr_2_screen', 
    image="instr_2.png", mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=[1.8, 1],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
instr_resp_2 = keyboard.Keyboard()

# --- Initialize components for Routine "letters" ---
letters_prac_screen = visual.ImageStim(
    win=win,
    name='letters_prac_screen', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=[1.8, 1],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
letters_prac_resp = keyboard.Keyboard()

# --- Initialize components for Routine "Instr_3" ---
instr_3_screen = visual.ImageStim(
    win=win,
    name='instr_3_screen', 
    image="instr_3.png", mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=[1.8, 1],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
instr_resp_3 = keyboard.Keyboard()

# --- Initialize components for Routine "Instr_4" ---
instr_4_screen = visual.ImageStim(
    win=win,
    name='instr_4_screen', 
    image="instr_4.png", mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=[1.8, 1],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
instr_resp_4 = keyboard.Keyboard()

# --- Initialize components for Routine "prac_trial" ---
prac_fixation = visual.TextStim(win=win, name='prac_fixation',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
prac_fixation2 = visual.TextStim(win=win, name='prac_fixation2',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
prac_stim = visual.ImageStim(
    win=win,
    name='prac_stim', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=[1.8, 1],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# --- Initialize components for Routine "Instr_5" ---
instr_5_screen = visual.ImageStim(
    win=win,
    name='instr_5_screen', 
    image="instr_5.png", mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.8, 1.0),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
instr_resp_5 = keyboard.Keyboard()

# --- Initialize components for Routine "prac_trial" ---
prac_fixation = visual.TextStim(win=win, name='prac_fixation',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
prac_fixation2 = visual.TextStim(win=win, name='prac_fixation2',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
prac_stim = visual.ImageStim(
    win=win,
    name='prac_stim', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=[1.8, 1],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# --- Initialize components for Routine "well_done" ---
well_done_screen = visual.ImageStim(
    win=win,
    name='well_done_screen', 
    image="well_done.png", mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.8, 1.0),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "Finished" ---
finished_screen = visual.ImageStim(
    win=win,
    name='finished_screen', 
    image="finished.png", mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.8,1.0),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_2 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Welcome" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
intr_resp.keys = []
intr_resp.rt = []
_intr_resp_allKeys = []
# keep track of which components have finished
WelcomeComponents = [welcome_screen, intr_resp]
for thisComponent in WelcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Welcome" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcome_screen* updates
    if welcome_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_screen.frameNStart = frameN  # exact frame index
        welcome_screen.tStart = t  # local t and not account for scr refresh
        welcome_screen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_screen, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'welcome_screen.started')
        welcome_screen.setAutoDraw(True)
    
    # *intr_resp* updates
    waitOnFlip = False
    if intr_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intr_resp.frameNStart = frameN  # exact frame index
        intr_resp.tStart = t  # local t and not account for scr refresh
        intr_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intr_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'intr_resp.started')
        intr_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(intr_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(intr_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if intr_resp.status == STARTED and not waitOnFlip:
        theseKeys = intr_resp.getKeys(keyList=['right'], waitRelease=False)
        _intr_resp_allKeys.extend(theseKeys)
        if len(_intr_resp_allKeys):
            intr_resp.keys = _intr_resp_allKeys[-1].name  # just the last key pressed
            intr_resp.rt = _intr_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Welcome" ---
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if intr_resp.keys in ['', [], None]:  # No response was made
    intr_resp.keys = None
thisExp.addData('intr_resp.keys',intr_resp.keys)
if intr_resp.keys != None:  # we had a response
    thisExp.addData('intr_resp.rt', intr_resp.rt)
thisExp.nextEntry()
# the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Instr_1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
instr_resp_1.keys = []
instr_resp_1.rt = []
_instr_resp_1_allKeys = []
# keep track of which components have finished
Instr_1Components = [instr_1_screen, instr_resp_1]
for thisComponent in Instr_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Instr_1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_1_screen* updates
    if instr_1_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_1_screen.frameNStart = frameN  # exact frame index
        instr_1_screen.tStart = t  # local t and not account for scr refresh
        instr_1_screen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_1_screen, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instr_1_screen.started')
        instr_1_screen.setAutoDraw(True)
    
    # *instr_resp_1* updates
    waitOnFlip = False
    if instr_resp_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_resp_1.frameNStart = frameN  # exact frame index
        instr_resp_1.tStart = t  # local t and not account for scr refresh
        instr_resp_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_resp_1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instr_resp_1.started')
        instr_resp_1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instr_resp_1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instr_resp_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instr_resp_1.status == STARTED and not waitOnFlip:
        theseKeys = instr_resp_1.getKeys(keyList=['right'], waitRelease=False)
        _instr_resp_1_allKeys.extend(theseKeys)
        if len(_instr_resp_1_allKeys):
            instr_resp_1.keys = _instr_resp_1_allKeys[-1].name  # just the last key pressed
            instr_resp_1.rt = _instr_resp_1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instr_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instr_1" ---
for thisComponent in Instr_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if instr_resp_1.keys in ['', [], None]:  # No response was made
    instr_resp_1.keys = None
thisExp.addData('instr_resp_1.keys',instr_resp_1.keys)
if instr_resp_1.keys != None:  # we had a response
    thisExp.addData('instr_resp_1.rt', instr_resp_1.rt)
thisExp.nextEntry()
# the Routine "Instr_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Instr_2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
instr_resp_2.keys = []
instr_resp_2.rt = []
_instr_resp_2_allKeys = []
# keep track of which components have finished
Instr_2Components = [instr_2_screen, instr_resp_2]
for thisComponent in Instr_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Instr_2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_2_screen* updates
    if instr_2_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_2_screen.frameNStart = frameN  # exact frame index
        instr_2_screen.tStart = t  # local t and not account for scr refresh
        instr_2_screen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_2_screen, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instr_2_screen.started')
        instr_2_screen.setAutoDraw(True)
    
    # *instr_resp_2* updates
    waitOnFlip = False
    if instr_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_resp_2.frameNStart = frameN  # exact frame index
        instr_resp_2.tStart = t  # local t and not account for scr refresh
        instr_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_resp_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instr_resp_2.started')
        instr_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instr_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instr_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instr_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = instr_resp_2.getKeys(keyList=['right'], waitRelease=False)
        _instr_resp_2_allKeys.extend(theseKeys)
        if len(_instr_resp_2_allKeys):
            instr_resp_2.keys = _instr_resp_2_allKeys[-1].name  # just the last key pressed
            instr_resp_2.rt = _instr_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instr_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instr_2" ---
for thisComponent in Instr_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if instr_resp_2.keys in ['', [], None]:  # No response was made
    instr_resp_2.keys = None
thisExp.addData('instr_resp_2.keys',instr_resp_2.keys)
if instr_resp_2.keys != None:  # we had a response
    thisExp.addData('instr_resp_2.rt', instr_resp_2.rt)
thisExp.nextEntry()
# the Routine "Instr_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
letters_loop = data.TrialHandler(nReps=3.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('letters_trials.csv'),
    seed=None, name='letters_loop')
thisExp.addLoop(letters_loop)  # add the loop to the experiment
thisLetters_loop = letters_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLetters_loop.rgb)
if thisLetters_loop != None:
    for paramName in thisLetters_loop:
        exec('{} = thisLetters_loop[paramName]'.format(paramName))

for thisLetters_loop in letters_loop:
    currentLoop = letters_loop
    # abbreviate parameter names if possible (e.g. rgb = thisLetters_loop.rgb)
    if thisLetters_loop != None:
        for paramName in thisLetters_loop:
            exec('{} = thisLetters_loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "letters" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    letters_prac_screen.setImage(stimulus)
    letters_prac_resp.keys = []
    letters_prac_resp.rt = []
    _letters_prac_resp_allKeys = []
    # keep track of which components have finished
    lettersComponents = [letters_prac_screen, letters_prac_resp]
    for thisComponent in lettersComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "letters" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *letters_prac_screen* updates
        if letters_prac_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            letters_prac_screen.frameNStart = frameN  # exact frame index
            letters_prac_screen.tStart = t  # local t and not account for scr refresh
            letters_prac_screen.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(letters_prac_screen, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'letters_prac_screen.started')
            letters_prac_screen.setAutoDraw(True)
        
        # *letters_prac_resp* updates
        waitOnFlip = False
        if letters_prac_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            letters_prac_resp.frameNStart = frameN  # exact frame index
            letters_prac_resp.tStart = t  # local t and not account for scr refresh
            letters_prac_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(letters_prac_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'letters_prac_resp.started')
            letters_prac_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(letters_prac_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(letters_prac_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if letters_prac_resp.status == STARTED and not waitOnFlip:
            theseKeys = letters_prac_resp.getKeys(keyList=['right'], waitRelease=False)
            _letters_prac_resp_allKeys.extend(theseKeys)
            if len(_letters_prac_resp_allKeys):
                letters_prac_resp.keys = _letters_prac_resp_allKeys[-1].name  # just the last key pressed
                letters_prac_resp.rt = _letters_prac_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in lettersComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "letters" ---
    for thisComponent in lettersComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if letters_prac_resp.keys in ['', [], None]:  # No response was made
        letters_prac_resp.keys = None
    letters_loop.addData('letters_prac_resp.keys',letters_prac_resp.keys)
    if letters_prac_resp.keys != None:  # we had a response
        letters_loop.addData('letters_prac_resp.rt', letters_prac_resp.rt)
    # the Routine "letters" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 3.0 repeats of 'letters_loop'


# --- Prepare to start Routine "Instr_3" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
instr_resp_3.keys = []
instr_resp_3.rt = []
_instr_resp_3_allKeys = []
# keep track of which components have finished
Instr_3Components = [instr_3_screen, instr_resp_3]
for thisComponent in Instr_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Instr_3" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_3_screen* updates
    if instr_3_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_3_screen.frameNStart = frameN  # exact frame index
        instr_3_screen.tStart = t  # local t and not account for scr refresh
        instr_3_screen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_3_screen, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instr_3_screen.started')
        instr_3_screen.setAutoDraw(True)
    
    # *instr_resp_3* updates
    waitOnFlip = False
    if instr_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_resp_3.frameNStart = frameN  # exact frame index
        instr_resp_3.tStart = t  # local t and not account for scr refresh
        instr_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_resp_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instr_resp_3.started')
        instr_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instr_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instr_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instr_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = instr_resp_3.getKeys(keyList=['right'], waitRelease=False)
        _instr_resp_3_allKeys.extend(theseKeys)
        if len(_instr_resp_3_allKeys):
            instr_resp_3.keys = _instr_resp_3_allKeys[-1].name  # just the last key pressed
            instr_resp_3.rt = _instr_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instr_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instr_3" ---
for thisComponent in Instr_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if instr_resp_3.keys in ['', [], None]:  # No response was made
    instr_resp_3.keys = None
thisExp.addData('instr_resp_3.keys',instr_resp_3.keys)
if instr_resp_3.keys != None:  # we had a response
    thisExp.addData('instr_resp_3.rt', instr_resp_3.rt)
thisExp.nextEntry()
# the Routine "Instr_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Instr_4" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
instr_resp_4.keys = []
instr_resp_4.rt = []
_instr_resp_4_allKeys = []
# keep track of which components have finished
Instr_4Components = [instr_4_screen, instr_resp_4]
for thisComponent in Instr_4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Instr_4" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_4_screen* updates
    if instr_4_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_4_screen.frameNStart = frameN  # exact frame index
        instr_4_screen.tStart = t  # local t and not account for scr refresh
        instr_4_screen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_4_screen, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instr_4_screen.started')
        instr_4_screen.setAutoDraw(True)
    
    # *instr_resp_4* updates
    waitOnFlip = False
    if instr_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_resp_4.frameNStart = frameN  # exact frame index
        instr_resp_4.tStart = t  # local t and not account for scr refresh
        instr_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_resp_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instr_resp_4.started')
        instr_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instr_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instr_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instr_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = instr_resp_4.getKeys(keyList=['right'], waitRelease=False)
        _instr_resp_4_allKeys.extend(theseKeys)
        if len(_instr_resp_4_allKeys):
            instr_resp_4.keys = _instr_resp_4_allKeys[-1].name  # just the last key pressed
            instr_resp_4.rt = _instr_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instr_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instr_4" ---
for thisComponent in Instr_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if instr_resp_4.keys in ['', [], None]:  # No response was made
    instr_resp_4.keys = None
thisExp.addData('instr_resp_4.keys',instr_resp_4.keys)
if instr_resp_4.keys != None:  # we had a response
    thisExp.addData('instr_resp_4.rt', instr_resp_4.rt)
thisExp.nextEntry()
# the Routine "Instr_4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('prac_trials.csv'),
    seed=None, name='practice')
thisExp.addLoop(practice)  # add the loop to the experiment
thisPractice = practice.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
if thisPractice != None:
    for paramName in thisPractice:
        exec('{} = thisPractice[paramName]'.format(paramName))

for thisPractice in practice:
    currentLoop = practice
    # abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
    if thisPractice != None:
        for paramName in thisPractice:
            exec('{} = thisPractice[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "prac_trial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code
    #k = event.waitKeys() # this will not start the trial unless there is input from the keyboard
        
    kb.clock.reset()
    
    key_up = 0
    key_down = 0
    
    count = count + 1
    
    jitter = random() * (1.5 - 1.0) + 1.0
    jitter = round(jitter, 1) # round to 1 decimal place
    
    stimulus_pulse_started = False
    stimulus_pulse_ended = False
    
    response_pulse_started = False
    response_pulse_ended = False
    
    stimulus_pulse_start_time = []
    response_pulse_start_time = []
    prac_stim.setImage(stimulus)
    # keep track of which components have finished
    prac_trialComponents = [prac_fixation, prac_fixation2, prac_stim]
    for thisComponent in prac_trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "prac_trial" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code
        remainingKeys = kb.getKeys(keyList=['space', 'right'], waitRelease=True, clear=True)
        
        pressedKeys = kb.getKeys(keyList=['space'], waitRelease=False, clear=True)
        
        if pressedKeys:
            for thisKey in pressedKeys:
                if thisKey.name == 'space':
                    key_down = 1
        
        if remainingKeys:
            for thisKey in remainingKeys:
                if thisKey.name == 'space': 
                    if thisKey.duration: #if the key has been lifted
                        method_1 = kb.clock.getTime() #current time on the kb clock
                        method_2 = thisKey.duration # this gets the time from the key pressed event to the key lift event (will include the 2 seconds of core.wait)
                        method_x = thisKey.duration + thisKey.tDown #the global time the key was pressed down + the time duration before it was released
                        key_up = 1
                        kb.clearEvents() #clear the key events
                elif thisKey.name == 'right':
                    kb.clearEvents()
                    continueRoutine = False
        
        
        if prac_stim.status == STARTED and not stimulus_pulse_started: #Change 'stimulus' to match the name of the component that you want to send the trigger for
            win.callOnFlip(port.write, str.encode('1'))
            stimulus_pulse_start_time = globalClock.getTime()
            stimulus_pulse_started  = True
        
        if stimulus_pulse_started and not stimulus_pulse_ended:
                if globalClock.getTime() - stimulus_pulse_start_time >= 0.005:
                    win.callOnFlip(port.write,  str.encode('0'))
                    stimulus_pulse_ended = True
        
        if key_up == 1 and not response_pulse_started: #Change 'stimulus' to match the name of the component that you want to send the trigger for
            win.callOnFlip(port.write, str.encode('2'))
            response_pulse_start_time = globalClock.getTime()
            response_pulse_started  = True
        
        if response_pulse_started and not response_pulse_ended:
                if globalClock.getTime() - response_pulse_start_time >= 0.005:
                    win.callOnFlip(port.write,  str.encode('0'))
                    response_pulse_ended = True
        
        # *prac_fixation* updates
        if prac_fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prac_fixation.frameNStart = frameN  # exact frame index
            prac_fixation.tStart = t  # local t and not account for scr refresh
            prac_fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_fixation, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prac_fixation.started')
            prac_fixation.setAutoDraw(True)
        if prac_fixation.status == STARTED:  # only update if drawing
            prac_fixation.setText('+', log=False)
        
        # *prac_fixation2* updates
        if prac_fixation2.status == NOT_STARTED and key_down == 1:
            # keep track of start time/frame for later
            prac_fixation2.frameNStart = frameN  # exact frame index
            prac_fixation2.tStart = t  # local t and not account for scr refresh
            prac_fixation2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_fixation2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prac_fixation2.started')
            prac_fixation2.setAutoDraw(True)
        if prac_fixation2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > prac_fixation2.tStartRefresh + jitter-frameTolerance:
                # keep track of stop time/frame for later
                prac_fixation2.tStop = t  # not accounting for scr refresh
                prac_fixation2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prac_fixation2.stopped')
                prac_fixation2.setAutoDraw(False)
        
        # *prac_stim* updates
        if prac_stim.status == NOT_STARTED and prac_fixation2.status == FINISHED:
            # keep track of start time/frame for later
            prac_stim.frameNStart = frameN  # exact frame index
            prac_stim.tStart = t  # local t and not account for scr refresh
            prac_stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_stim, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prac_stim.started')
            prac_stim.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prac_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prac_trial" ---
    for thisComponent in prac_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code
    thisExp.addData('Trigger_Stim_Start', stimulus_pulse_start_time)
    thisExp.addData('Trigger_Resp_Start', response_pulse_start_time)
    thisExp.addData('jitter', jitter)
    thisExp.addData('method_x', method_x) # The current time on the kb clock
    thisExp.addData('method_1', method_1) # The overall time when the button was released
    thisExp.addData('method_2', method_2) # How long was the key pressed for
    thisExp.addData("button", thisKey.name)
    thisExp.addData("button_time", thisKey.tDown)
    thisExp.addData("button_rt", thisKey.rt)
    
    # the Routine "prac_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'practice'


# --- Prepare to start Routine "Instr_5" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
instr_resp_5.keys = []
instr_resp_5.rt = []
_instr_resp_5_allKeys = []
# keep track of which components have finished
Instr_5Components = [instr_5_screen, instr_resp_5]
for thisComponent in Instr_5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Instr_5" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_5_screen* updates
    if instr_5_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_5_screen.frameNStart = frameN  # exact frame index
        instr_5_screen.tStart = t  # local t and not account for scr refresh
        instr_5_screen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_5_screen, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instr_5_screen.started')
        instr_5_screen.setAutoDraw(True)
    
    # *instr_resp_5* updates
    waitOnFlip = False
    if instr_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_resp_5.frameNStart = frameN  # exact frame index
        instr_resp_5.tStart = t  # local t and not account for scr refresh
        instr_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_resp_5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instr_resp_5.started')
        instr_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instr_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instr_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instr_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = instr_resp_5.getKeys(keyList=['right'], waitRelease=False)
        _instr_resp_5_allKeys.extend(theseKeys)
        if len(_instr_resp_5_allKeys):
            instr_resp_5.keys = _instr_resp_5_allKeys[-1].name  # just the last key pressed
            instr_resp_5.rt = _instr_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instr_5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instr_5" ---
for thisComponent in Instr_5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if instr_resp_5.keys in ['', [], None]:  # No response was made
    instr_resp_5.keys = None
thisExp.addData('instr_resp_5.keys',instr_resp_5.keys)
if instr_resp_5.keys != None:  # we had a response
    thisExp.addData('instr_resp_5.rt', instr_resp_5.rt)
thisExp.nextEntry()
# the Routine "Instr_5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
blocks = data.TrialHandler(nReps=5.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='blocks')
thisExp.addLoop(blocks)  # add the loop to the experiment
thisBlock = blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

for thisBlock in blocks:
    currentLoop = blocks
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=4.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('prac_trials.csv'),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "prac_trial" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code
        #k = event.waitKeys() # this will not start the trial unless there is input from the keyboard
            
        kb.clock.reset()
        
        key_up = 0
        key_down = 0
        
        count = count + 1
        
        jitter = random() * (1.5 - 1.0) + 1.0
        jitter = round(jitter, 1) # round to 1 decimal place
        
        stimulus_pulse_started = False
        stimulus_pulse_ended = False
        
        response_pulse_started = False
        response_pulse_ended = False
        
        stimulus_pulse_start_time = []
        response_pulse_start_time = []
        prac_stim.setImage(stimulus)
        # keep track of which components have finished
        prac_trialComponents = [prac_fixation, prac_fixation2, prac_stim]
        for thisComponent in prac_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "prac_trial" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code
            remainingKeys = kb.getKeys(keyList=['space', 'right'], waitRelease=True, clear=True)
            
            pressedKeys = kb.getKeys(keyList=['space'], waitRelease=False, clear=True)
            
            if pressedKeys:
                for thisKey in pressedKeys:
                    if thisKey.name == 'space':
                        key_down = 1
            
            if remainingKeys:
                for thisKey in remainingKeys:
                    if thisKey.name == 'space': 
                        if thisKey.duration: #if the key has been lifted
                            method_1 = kb.clock.getTime() #current time on the kb clock
                            method_2 = thisKey.duration # this gets the time from the key pressed event to the key lift event (will include the 2 seconds of core.wait)
                            method_x = thisKey.duration + thisKey.tDown #the global time the key was pressed down + the time duration before it was released
                            key_up = 1
                            kb.clearEvents() #clear the key events
                    elif thisKey.name == 'right':
                        kb.clearEvents()
                        continueRoutine = False
            
            
            if prac_stim.status == STARTED and not stimulus_pulse_started: #Change 'stimulus' to match the name of the component that you want to send the trigger for
                win.callOnFlip(port.write, str.encode('1'))
                stimulus_pulse_start_time = globalClock.getTime()
                stimulus_pulse_started  = True
            
            if stimulus_pulse_started and not stimulus_pulse_ended:
                    if globalClock.getTime() - stimulus_pulse_start_time >= 0.005:
                        win.callOnFlip(port.write,  str.encode('0'))
                        stimulus_pulse_ended = True
            
            if key_up == 1 and not response_pulse_started: #Change 'stimulus' to match the name of the component that you want to send the trigger for
                win.callOnFlip(port.write, str.encode('2'))
                response_pulse_start_time = globalClock.getTime()
                response_pulse_started  = True
            
            if response_pulse_started and not response_pulse_ended:
                    if globalClock.getTime() - response_pulse_start_time >= 0.005:
                        win.callOnFlip(port.write,  str.encode('0'))
                        response_pulse_ended = True
            
            # *prac_fixation* updates
            if prac_fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                prac_fixation.frameNStart = frameN  # exact frame index
                prac_fixation.tStart = t  # local t and not account for scr refresh
                prac_fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prac_fixation, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prac_fixation.started')
                prac_fixation.setAutoDraw(True)
            if prac_fixation.status == STARTED:  # only update if drawing
                prac_fixation.setText('+', log=False)
            
            # *prac_fixation2* updates
            if prac_fixation2.status == NOT_STARTED and key_down == 1:
                # keep track of start time/frame for later
                prac_fixation2.frameNStart = frameN  # exact frame index
                prac_fixation2.tStart = t  # local t and not account for scr refresh
                prac_fixation2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prac_fixation2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prac_fixation2.started')
                prac_fixation2.setAutoDraw(True)
            if prac_fixation2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > prac_fixation2.tStartRefresh + jitter-frameTolerance:
                    # keep track of stop time/frame for later
                    prac_fixation2.tStop = t  # not accounting for scr refresh
                    prac_fixation2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'prac_fixation2.stopped')
                    prac_fixation2.setAutoDraw(False)
            
            # *prac_stim* updates
            if prac_stim.status == NOT_STARTED and prac_fixation2.status == FINISHED:
                # keep track of start time/frame for later
                prac_stim.frameNStart = frameN  # exact frame index
                prac_stim.tStart = t  # local t and not account for scr refresh
                prac_stim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prac_stim, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prac_stim.started')
                prac_stim.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in prac_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "prac_trial" ---
        for thisComponent in prac_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from code
        thisExp.addData('Trigger_Stim_Start', stimulus_pulse_start_time)
        thisExp.addData('Trigger_Resp_Start', response_pulse_start_time)
        thisExp.addData('jitter', jitter)
        thisExp.addData('method_x', method_x) # The current time on the kb clock
        thisExp.addData('method_1', method_1) # The overall time when the button was released
        thisExp.addData('method_2', method_2) # How long was the key pressed for
        thisExp.addData("button", thisKey.name)
        thisExp.addData("button_time", thisKey.tDown)
        thisExp.addData("button_rt", thisKey.rt)
        
        # the Routine "prac_trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 4.0 repeats of 'trials'
    
    
    # --- Prepare to start Routine "well_done" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    well_doneComponents = [well_done_screen, key_resp]
    for thisComponent in well_doneComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "well_done" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *well_done_screen* updates
        if well_done_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            well_done_screen.frameNStart = frameN  # exact frame index
            well_done_screen.tStart = t  # local t and not account for scr refresh
            well_done_screen.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(well_done_screen, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'well_done_screen.started')
            well_done_screen.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.started')
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['right'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in well_doneComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "well_done" ---
    for thisComponent in well_doneComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    blocks.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        blocks.addData('key_resp.rt', key_resp.rt)
    # the Routine "well_done" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 5.0 repeats of 'blocks'


# --- Prepare to start Routine "Finished" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
FinishedComponents = [finished_screen, key_resp_2]
for thisComponent in FinishedComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Finished" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *finished_screen* updates
    if finished_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finished_screen.frameNStart = frameN  # exact frame index
        finished_screen.tStart = t  # local t and not account for scr refresh
        finished_screen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finished_screen, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'finished_screen.started')
        finished_screen.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_2.started')
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['y','n','left','right','space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FinishedComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Finished" ---
for thisComponent in FinishedComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "Finished" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
# Run 'End Experiment' code from code
port.close()
# Run 'End Experiment' code from code
port.close()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
