%% Face Detection in a Video
% This example uses the Viola-Jones Algorithm to detect a face in the
% video. It shows how to read, write, process and display videos.
% Copyright 2018 The MathWorks, Inc.
%% Read a video into MATLAB
videoFileReader = VideoReader('tilted_face.avi');
myVideo = VideoWriter('myFile.avi');
depVideoPlayer = vision.DeployableVideoPlayer;
% Initialize the Detector
faceDetector = vision.CascadeObjectDetector();
open(myVideo);
%% Detect faces in each frame
while hasFrame(videoFileReader)
    videoFrame = readFrame(videoFileReader);
    % Detect the face 
    bbox = faceDetector(videoFrame);
    % Insert a box around the detected face
    videoFrame = insertShape(videoFrame, 'Rectangle', bbox); 
    % Display video
    depVideoPlayer(videoFrame);
    % Write frame to a video
    writeVideo(myVideo, videoFrame);
    %pause(1/videoFileReader.FrameRate);
end
close(myVideo)


