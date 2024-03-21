% fsr_filter_testing.m
% 2024-3-18
% Author: Sarah Boyd
% Description: Calculates the gain and plots the filter data

clear 
clc

%% Import the data

file_name = "FSR_Filter_Data.xlsx";

if exist(file_name,"file") 
    
    opt=detectImportOptions(file_name);

    FSR1 = readtable(file_name,opt,'Sheet','FSR1');
    FSR2 = readtable(file_name,opt,'Sheet','FSR2');
    FSR3 = readtable(file_name,opt,'Sheet','FSR3');
    FSR4 = readtable(file_name,opt,'Sheet','FSR4');
    FSR5 = readtable(file_name,opt,'Sheet','FSR5');
    FSR6 = readtable(file_name,opt,'Sheet','FSR6');
    FSR7 = readtable(file_name,opt,'Sheet','FSR7');
    FSR8 = readtable(file_name,opt,'Sheet','FSR8');

else
    disp("Could not find data file")
    return
end

%% Plot signal for each FSR

freqs = [1 5 10 15 20 25];


% ******************** FSR1 *************************
figure(1) % this is for FSR 1

plot_ind = 2;

for i = 1:6
    subplot(3,2,i)
    plot(FSR1{:,1}, FSR1{:,plot_ind})
    hold on
    plot(FSR1{:,1}, FSR1{:,plot_ind + 1})
    hold off
    legend("FSR1-IN", "FSR1-OUT")
    ylim([-0.5,2.5])
    xlabel("Time (s)")
    ylabel("Voltage (V)")

    title(['FSR1 Filter output with a ' num2str(freqs(i)) ' Hz sinusoid input'])

    plot_ind = plot_ind + 2;
end


% ******************** FSR2 *************************
figure(2) % this is for FSR 2

plot_ind = 2;

for i = 1:6
    subplot(3,2,i)
    plot(FSR2{:,1}, FSR2{:,plot_ind})
    hold on
    plot(FSR2{:,1}, FSR2{:,plot_ind + 1})
    hold off
    legend("FSR2-IN", "FSR2-OUT")
    ylim([-0.5,2.5])
    xlabel("Time (s)")
    ylabel("Voltage (V)")

    title(['FSR2 Filter output with a ' num2str(freqs(i)) ' Hz sinusoid input'])

    plot_ind = plot_ind + 2;
end


% ******************** FSR3 *************************
figure(3) % this is for FSR 3

plot_ind = 2;

for i = 1:6
    subplot(3,2,i)
    plot(FSR3{:,1}, FSR3{:,plot_ind})
    hold on
    plot(FSR3{:,1}, FSR3{:,plot_ind + 1})
    hold off
    legend("FSR3-IN", "FSR3-OUT")
    ylim([-0.5,2.5])
    xlabel("Time (s)")
    ylabel("Voltage (V)")

    title(['FSR3 Filter output with a ' num2str(freqs(i)) ' Hz sinusoid input'])

    plot_ind = plot_ind + 2;
end


% ******************** FSR4 *************************
figure(4) % this is for FSR 4

plot_ind = 2;

for i = 1:6
    subplot(3,2,i)
    plot(FSR4{:,1}, FSR4{:,plot_ind})
    hold on
    plot(FSR4{:,1}, FSR4{:,plot_ind + 1})
    hold off
    legend("FSR4-IN", "FSR4-OUT")
    ylim([-0.5,2.5])
    xlabel("Time (s)")
    ylabel("Voltage (V)")

    title(['FSR4 Filter output with a ' num2str(freqs(i)) ' Hz sinusoid input'])

    plot_ind = plot_ind + 2;
end


% ******************** FSR5 *************************
figure(5) % this is for FSR 5

plot_ind = 2;

for i = 1:6
    subplot(3,2,i)
    plot(FSR5{:,1}, FSR5{:,plot_ind})
    hold on
    plot(FSR5{:,1}, FSR5{:,plot_ind + 1})
    hold off
    legend("FSR5-IN", "FSR5-OUT")
    ylim([-0.5,2.5])
    xlabel("Time (s)")
    ylabel("Voltage (V)")

    title(['FSR5 Filter output with a ' num2str(freqs(i)) ' Hz sinusoid input'])

    plot_ind = plot_ind + 2;
end


% ******************** FSR6 *************************
figure(6) % this is for FSR 6

plot_ind = 2;

for i = 1:6
    subplot(3,2,i)
    plot(FSR6{:,1}, FSR6{:,plot_ind})
    hold on
    plot(FSR6{:,1}, FSR6{:,plot_ind + 1})
    hold off
    legend("FSR6-IN", "FSR6-OUT")
    ylim([-0.5,3.5])
    xlabel("Time (s)")
    ylabel("Voltage (V)")

    title(['FSR6 Filter output with a ' num2str(freqs(i)) ' Hz sinusoid input'])

    plot_ind = plot_ind + 2;
end


% ******************** FSR7 *************************
figure(7) % this is for FSR 7

plot_ind = 2;

for i = 1:6
    subplot(3,2,i)
    plot(FSR7{:,1}, FSR7{:,plot_ind})
    hold on
    plot(FSR7{:,1}, FSR7{:,plot_ind + 1})
    hold off
    legend("FSR7-IN", "FSR7-OUT")
    ylim([-0.5,2.5])
    xlabel("Time (s)")
    ylabel("Voltage (V)")

    title(['FSR7 Filter output with a ' num2str(freqs(i)) ' Hz sinusoid input'])

    plot_ind = plot_ind + 2;
end


% ******************** FSR8 *************************
figure(8) % this is for FSR 8

plot_ind = 2;

for i = 1:6
    subplot(3,2,i)
    plot(FSR8{:,1}, FSR8{:,plot_ind})
    hold on
    plot(FSR8{:,1}, FSR8{:,plot_ind + 1})
    hold off
    legend("FSR8-IN", "FSR8-OUT")
    ylim([-0.5,2.5])
    xlabel("Time (s)")
    ylabel("Voltage (V)")

    title(['FSR8 Filter output with a ' num2str(freqs(i)) ' Hz sinusoid input'])

    plot_ind = plot_ind + 2;
end


%% Calculate gain for each signal at each frequency 

% ******************** FSR1 *************************
sig_ind = 2;

for i = 1:6
    max_in1(i) = max(FSR1{:,sig_ind});
    max_out1(i) = max(FSR1{:,sig_ind+1});

    sig_ind = sig_ind + 2;
end

gain1 = 20*log10(max_out1./max_in1);

T1 = array2table(gain1, 'VariableNames', {'1 Hz', '5 Hz', '10 Hz', ...
    '15 Hz', '20 Hz', '25 Hz'}, 'RowNames', {'Gain'});
disp('FSR1 filtering circuit:')
disp(T1)


% ******************** FSR2 *************************
sig_ind = 2;

for i = 1:6
    max_in2(i) = max(FSR2{:,sig_ind});
    max_out2(i) = max(FSR2{:,sig_ind+1});

    sig_ind = sig_ind + 2;
end

gain2 = 20*log10(max_out2./max_in2);

T2 = array2table(gain2, 'VariableNames', {'1 Hz', '5 Hz', '10 Hz', ...
    '15 Hz', '20 Hz', '25 Hz'}, 'RowNames', {'Gain'});
disp('FSR2 filtering circuit:')
disp(T2)


% ******************** FSR3 *************************
sig_ind = 2;

for i = 1:6
    max_in3(i) = max(FSR3{:,sig_ind});
    max_out3(i) = max(FSR3{:,sig_ind+1});

    sig_ind = sig_ind + 2;
end

gain3 = 20*log10(max_out3./max_in3);

T3 = array2table(gain3, 'VariableNames', {'1 Hz', '5 Hz', '10 Hz', ...
    '15 Hz', '20 Hz', '25 Hz'}, 'RowNames', {'Gain'});
disp('FSR3 filtering circuit:')
disp(T3)

% ******************** FSR4 *************************
sig_ind = 2;

for i = 1:6
    max_in4(i) = max(FSR4{:,sig_ind});
    max_out4(i) = max(FSR4{:,sig_ind+1});

    sig_ind = sig_ind + 2;
end

gain4 = 20*log10(max_out4./max_in4);

T4 = array2table(gain4, 'VariableNames', {'1 Hz', '5 Hz', '10 Hz', ...
    '15 Hz', '20 Hz', '25 Hz'}, 'RowNames', {'Gain'});
disp('FSR4 filtering circuit:')
disp(T4)

% ******************** FSR5 *************************
sig_ind = 2;

for i = 1:6
    max_in5(i) = max(FSR5{:,sig_ind});
    max_out5(i) = max(FSR5{:,sig_ind+1});

    sig_ind = sig_ind + 2;
end

gain5 = 20*log10(max_out5./max_in5);

T5 = array2table(gain5, 'VariableNames', {'1 Hz', '5 Hz', '10 Hz', ...
    '15 Hz', '20 Hz', '25 Hz'}, 'RowNames', {'Gain'});
disp('FSR5 filtering circuit:')
disp(T5)

% ******************** FSR6 *************************
sig_ind = 2;

for i = 1:6
    max_in6(i) = max(FSR6{:,sig_ind});
    max_out6(i) = max(FSR6{:,sig_ind+1});

    sig_ind = sig_ind + 2;
end

gain6 = 20*log10(max_out6./max_in6);

T6 = array2table(gain6, 'VariableNames', {'1 Hz', '5 Hz', '10 Hz', ...
    '15 Hz', '20 Hz', '25 Hz'}, 'RowNames', {'Gain'});
disp('FSR6 filtering circuit:')
disp(T6)

% ******************** FSR7 *************************
sig_ind = 2;

for i = 1:6
    max_in7(i) = max(FSR7{:,sig_ind});
    max_out7(i) = max(FSR7{:,sig_ind+1});

    sig_ind = sig_ind + 2;
end

gain7 = 20*log10(max_out7./max_in7);

T7 = array2table(gain7, 'VariableNames', {'1 Hz', '5 Hz', '10 Hz', ...
    '15 Hz', '20 Hz', '25 Hz'}, 'RowNames', {'Gain'});
disp('FSR7 filtering circuit:')
disp(T7)

% ******************** FSR8 *************************
sig_ind = 2;

for i = 1:6
    max_in8(i) = max(FSR8{:,sig_ind});
    max_out8(i) = max(FSR8{:,sig_ind+1});

    sig_ind = sig_ind + 2;
end

gain8 = 20*log10(max_out8./max_in8);

T8 = array2table(gain8, 'VariableNames', {'1 Hz', '5 Hz', '10 Hz', ...
    '15 Hz', '20 Hz', '25 Hz'}, 'RowNames', {'Gain'});
disp('FSR8 filtering circuit:')
disp(T8)
