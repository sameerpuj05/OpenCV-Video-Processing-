%% Slider Effect in a Video
% This example shows how to create the slider effect in a video. One part
% of it detects edges using the Canny Method.
% Copyright 2018 The MathWorks, Inc.
%% Read the video into MATLAB 
videoFileReader = VideoReader('robo.mp4');
% This value determine the speed of the sliding effect
speed = 10;
col = videoFileReader.width;
% Display video
depVideoPlayer = vision.DeployableVideoPlayer;
%% Process each frame
while hasFrame(videoFileReader)
% Left to Right
    for idx = 1:speed:col
        videoFrame = readFrame(videoFileReader);
        % Detect edges in the grayscale image
        edgeFrame = edge(rgb2gray(videoFrame),'canny');
        edgeFrame = edgeFrame * 255; 
        % Part of the Input Frame
        n1 = videoFrame(:, 1 : idx,:);
        % Part of the Edge Detected Frame
        n2 = edgeFrame(:, idx+1 : col );
        % Concatenating them together
        finalFrame = [n1 cat(3,n2,n2,n2)];
        depVideoPlayer(finalFrame);
    end    
% Right to Left
    for idx = col:-speed:1
        videoFrame = readFrame(videoFileReader);
        % Detect edges in the grayscale image
        edgeFrame = edge(rgb2gray(videoFrame),'canny');
        edgeFrame = edgeFrame * 255;  
        % Part of the Input Frame
        n1 = videoFrame(:, 1 : idx,:);
        % Part of the Edge Detected Frame
        n2 = edgeFrame(:, idx+1 : col );
        % Concatenating them together
        finalFrame = [n1 cat(3,n2,n2,n2)];
        depVideoPlayer(finalFrame);
    end

end

  

% for idx=1:10:e
%     n1 = i(:, 1 : idx);
%     n2 = i2(:, idx+1 : e );
%     imshow([n1 im2uint8(n2)])
% 
% end
% for idx=e:-10:1
%     n1 = i(:, 1 : idx);
%     n2 = i2(:, idx+1 : e );
%     imshow([n1 im2uint8(n2)])
% 
% end

