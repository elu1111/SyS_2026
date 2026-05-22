# Data

[sound_1, fs_1] = audioread('440Hz_44100Hz_16bit_05sec.wav');
[sound_2, fs_2] = audioread('440Hz_piano.wav');
[sound_3, fs_3] = audioread('440Hz_violin_A4.wav');

# 
disp('frequency, size:')
disp('pure tone (frequency, size): '); disp(fs_1); disp(size(sound_1));
disp('piano     (frequency, size): ');     disp(fs_2); disp(size(sound_2));
disp('violin    (frequency, size): ');    disp(fs_3); disp(size(sound_3));

# sliding window
start = 1.2;
stop = 1.211;
channel = 0;

# sound fragments
dt_1 = 1 / fs_1;
t_1 = (start:dt_1:stop)';
samples = length(t_1) - 1;
fragment_1 = sound_1(floor(start/dt_1):floor(start/dt_1) + samples);

dt_2 = 1 / fs_2;
t_2 = (start:dt_2:stop)';
samples = length(t_2) - 1;
fragment_2 = sound_2(floor(start/dt_2):floor(start/dt_2) + samples);

dt_3 = 1 / fs_3;
t_3 = (start:dt_3:stop)';
samples = length(t_3) - 1;
fragment_3 = sound_3(floor(start/dt_3): floor(start/dt_3) + samples);

figure(1)
subplot(311)
plot(t_1, fragment_1)
ylabel('pure tone')
subplot(312)
plot(t_2, fragment_2)
ylabel('piano')
subplot(313)
plot(t_3, fragment_3)
ylabel('violin')
xlabel('t secs.')

[Xw_1, w_1] = myfft(fragment_1, dt_1);
[Xw_2, w_2] = myfft(fragment_2, dt_2);
[Xw_3, w_3] = myfft(fragment_3, dt_3);

figure(2)
subplot(311)
plot(w_1, abs(Xw_1))
ylabel('pure tone')
subplot(312)
plot(w_2, abs(Xw_2))
ylabel('piano')
subplot(313)
plot(w_3, abs(Xw_3))
ylabel('violin')
xlabel('\omega radians/secs')

