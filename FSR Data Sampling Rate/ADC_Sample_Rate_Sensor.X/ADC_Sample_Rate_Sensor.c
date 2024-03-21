/*
 * File:   ADC_Sample_Rate_Sensor.c
 * Author: sarah
 *
 * Created on March 17, 2024, 11:06 AM
 */

// FOSCSEL
#pragma config FNOSC = FRC              // Oscillator Source Selection (Internal Fast RC (FRC))
#pragma config IESO = ON                // Two-speed Oscillator Start-up Enable bit (Start up device with FRC, then switch to user-selected oscillator source)

// FOSC
#pragma config POSCMD = NONE            // Primary Oscillator Mode Select bits (Primary Oscillator disabled)
#pragma config OSCIOFNC = OFF           // OSC2 Pin Function bit (OSC2 is clock output)
#pragma config FCKSM = CSECMD           // Clock Switching Mode bits (Clock switching is enabled,Fail-safe Clock Monitor is disabled)
#pragma config PLLKEN = ON              // PLL Lock Status Control (PLL lock signal will be used to disable PLL clock output if lock is lost)
#pragma config XTCFG = G3               // XT Config (24-32 MHz crystals)
#pragma config XTBST = ENABLE           // XT Boost (Boost the kick-start)

// FWDT
#pragma config RWDTPS = PS2147483648    // Run Mode Watchdog Timer Post Scaler select bits (1:2147483648)
#pragma config RCLKSEL = LPRC           // Watchdog Timer Clock Select bits (Always use LPRC)
#pragma config WINDIS = ON              // Watchdog Timer Window Enable bit (Watchdog Timer operates in Non-Window mode)
#pragma config WDTWIN = WIN25           // Watchdog Timer Window Select bits (WDT Window is 25% of WDT period)
#pragma config SWDTPS = PS2147483648    // Sleep Mode Watchdog Timer Post Scaler select bits (1:2147483648)
#pragma config FWDTEN = ON_SW           // Watchdog Timer Enable bit (WDT controlled via SW, use WDTCON.ON bit)

// FPOR
#pragma config BISTDIS = DISABLED       // Memory BIST Feature Disable (mBIST on reset feature disabled)

// FICD
#pragma config ICS = PGD1               // ICD Communication Channel Select bits (Communicate on PGC3 and PGD3)
#pragma config JTAGEN = OFF             // JTAG Enable bit (JTAG is disabled)
#pragma config NOBTSWP = DISABLED       // BOOTSWP instruction disable bit (BOOTSWP instruction is disabled)

// FDEVOPT
#pragma config ALTI2C1 = OFF            // Alternate I2C1 Pin bit (I2C1 mapped to SDA1/SCL1 pins)
#pragma config ALTI2C2 = OFF            // Alternate I2C2 Pin bit (I2C2 mapped to SDA2/SCL2 pins)
#pragma config ALTI2C3 = OFF            // Alternate I2C3 Pin bit (I2C3 mapped to SDA3/SCL3 pins)
#pragma config SMBEN = SMBUS            // SM Bus Enable (SMBus input threshold is enabled)
#pragma config SPI2PIN = PPS            // SPI2 Pin Select bit (SPI2 uses I/O remap (PPS) pins)

// FALTREG
#pragma config CTXT1 = OFF              // Specifies Interrupt Priority Level (IPL) Associated to Alternate Working Register 1 bits (Not Assigned)
#pragma config CTXT2 = OFF              // Specifies Interrupt Priority Level (IPL) Associated to Alternate Working Register 2 bits (Not Assigned)
#pragma config CTXT3 = OFF              // Specifies Interrupt Priority Level (IPL) Associated to Alternate Working Register 3 bits (Not Assigned)
#pragma config CTXT4 = OFF              // Specifies Interrupt Priority Level (IPL) Associated to Alternate Working Register 4 bits (Not Assigned)

#define FCY 60000000

//CLOCK DEFINITIONS
#define POSTD1 2
#define POSTD2 1
#define PRE_PLL 1
#define FBD_PLL 60

volatile int dataAN0;
volatile int dataAN3;
volatile int dataAN4;
volatile int dataAN5;
volatile float fsr_o1;
volatile float fsr_o2;
volatile float fsr_o3;
volatile float fsr_o4;
volatile float ADC_Data_o1[250];
volatile float ADC_Data_o2[250];
volatile float ADC_Data_o3[250];
volatile float ADC_Data_o4[250];
int ind_count1 = 0;
int ind_count2 = 0;
int ind_count3 = 0;
int ind_count4 = 0;


//ADD IN FUNCTIONS AND ISRs
void init_Timer1(void);
void __attribute__((interrupt, no_auto_psv)) _ADCAN1Interrupt(void);
void __attribute__((interrupt, no_auto_psv)) _ADCAN0Interrupt(void);
void __attribute__((interrupt, no_auto_psv)) _T1Interrupt(void);

#include <xc.h>
#include "libpic30.h"


//ADC DEFINITIONS
#define AN1 ANSELAbits.ANSELA0
#define AN1_pin TRISAbits.TRISA0
#define AN3 ANSELAbits.ANSELA3
#define AN3_pin TRISAbits.TRISA3
#define AN4 ANSELAbits.ANSELA4
#define AN4_pin TRISAbits.TRISA4
#define AN5 ANSELBbits.ANSELB0
#define AN5_pin TRISBbits.TRISB0

//ADC VARIABLES
volatile int dataAN0;
volatile int dataAN1;
volatile int dataAN2;
volatile int dataAN3;
volatile float voltage0;
volatile float voltage1;
volatile float voltage2;
volatile float voltage3;

void init_ADC(void);
void EnableADC(void);

int main(void) {
    
    //SETUP CLOCK
    // CPU clock is 8MHz*60/1/1/2/2/2 = 60MIPS
    _POST1DIV = POSTD1; // :2
    _POST2DIV = POSTD2; // :1
    _PLLPRE = PRE_PLL; // :1
    PLLFBD = FBD_PLL; // x60
    __builtin_write_OSCCONH(1); // 1=FRCPLL
    __builtin_write_OSCCONL(1);
    while (_COSC != 1);
    while (OSCCONbits.LOCK != 1);
    
    
    //INITIATE TIMER, ADC, AND I2C
    init_ADC();
    init_Timer1();
    
    while(1){
        
        
    }
    
    return 0;
}


// ADC AN0 ISR
void __attribute__((interrupt, no_auto_psv)) _ADCAN0Interrupt(void)
{
    dataAN0 = ADCBUF0; // read conversion result
    fsr_o2 = (float)dataAN0 * (float)(3.3/(float)4096); //Convert digital to voltage value
    
    ADC_Data_o2[ind_count2] = fsr_o2;
    ind_count2++; 
    
    _ADCAN0IF = 0; // clear interrupt flag
}

void __attribute__((interrupt, no_auto_psv)) _ADCAN3Interrupt(void)
{
    dataAN1 = ADCBUF3; // read conversion result
    fsr_o4 = (float)dataAN1 * (float)(3.3/(float)4096); //Convert digital to voltage value
    
    ADC_Data_o4[ind_count4] = fsr_o4;
    ind_count4++; 
    
    IFS5bits.ADCAN3IF = 0; // clear interrupt flag
}

void __attribute__((interrupt, no_auto_psv)) _ADCAN4Interrupt(void)
{
    dataAN2 = ADCBUF4; // read conversion result
    fsr_o3 = (float)dataAN2 * (float)(3.3/(float)4096); //Convert digital to voltage value
    
    ADC_Data_o3[ind_count3] = fsr_o3;
    ind_count3++; 
    
    IFS5bits.ADCAN4IF = 0; // clear interrupt flag
}

void __attribute__((interrupt, no_auto_psv)) _ADCAN5Interrupt(void)
{
    dataAN3 = ADCBUF5; // read conversion result
    fsr_o1 = (float)dataAN3 * (float)(3.3/(float)4096); //Convert digital to voltage value
    
    ADC_Data_o1[ind_count1] = fsr_o1;
    ind_count1++; 
    
    IFS6bits.ADCAN5IF = 0; // clear interrupt flag
}


void __attribute__((interrupt, no_auto_psv)) _T1Interrupt(void) {
    ADCON3Lbits.SWCTRG = 1;//Enable ADC Read
    IFS0bits.T1IF = 0; //Clear flag
}

void init_Timer1(void) {
    
    T1CONbits.TON = 1;
    T1CONbits.TCKPS = 3;
    T1CONbits.TCS = 0;
    T1CONbits.TSYNC = 0;

    IPC0bits.T1IP = 1;
    IEC0bits.T1IE = 1;
    PR1 = 0x5000; //2048 clock cycle rollover
}

void init_ADC(void) {
    //set pins to ADC inputs
    
    AN1 = 1; //AN1 is analog
    AN1_pin = 1; //AN1 is input
    AN3 = 1;
    AN3_pin = 1;
    AN4 = 1;
    AN4_pin = 1;
    AN5 = 1;
    AN5_pin = 1;

    //configure the common ADC clock
    ADCON3Hbits.CLKSEL = 0;
    ADCON3Hbits.CLKDIV = 0; //no clock division (1:1)
    
    //configure the ADC core clocks
    ADCORE0Hbits.ADCS = 0; //clock divider (1:2)
    ADCORE1Hbits.ADCS = 0; //clock divider (1:2)
    ADCON2Lbits.SHRADCS = 0; //clock divider (1:2)
    
    //configure the ADC reference source
    ADCON3Lbits.REFSEL = 0; //AVdd is the voltage reference
    
    //set output format
    ADCON1Hbits.FORM = 0; //integer format
    
    //select input format
    ADMOD0Lbits.SIGN0 = 0; //unsigned
    ADMOD0Lbits.DIFF0 = 0; //single ended
    
    //set the ADC resolution
    ADCORE1Hbits.RES = 3; //12 bit resolution (dedicated core)
    ADCON1Hbits.SHRRES = 3; //12 bit resolution (shared core)
    
    //Enable ADC
    EnableADC();

    ADIELbits.IE0 = 1;
    ADIELbits.IE3 = 1;
    ADIELbits.IE4 = 1;
    ADIELbits.IE5 = 1;
    
    _ADCAN0IF = 0; // clear interrupt flag for AN0
    _ADCAN0IE = 1; // enable interrupt for AN0
    IFS5bits.ADCAN3IF = 0;
    IEC5bits.ADCAN3IE = 1;
    IFS5bits.ADCAN4IF = 0;
    IEC5bits.ADCAN4IE = 1;
    IFS6bits.ADCAN5IF = 0;
    IEC6bits.ADCAN5IE = 1;

    //set analog output triggers
    ADTRIG0Lbits.TRGSRC0 = 1; //Enable AN0 trigger
    ADTRIG0Hbits.TRGSRC3 = 1;
    ADTRIG1Lbits.TRGSRC4 = 1;
    ADTRIG1Lbits.TRGSRC5 = 1;
}

void EnableADC(void) {
    ADCON5Hbits.WARMTIME = 15; //set initialization time to maximum
    ADCON1Lbits.ADON = 1; //turn on the ADC module
    
    // Turn on and configure core 0
    ADCON5Lbits.C0PWR = 1;
    while(ADCON5Lbits.C0RDY == 0);
    ADCON3Hbits.C0EN = 1;
    
    //Turn on and configure core 1
    ADCON5Lbits.C1PWR = 1;
    while(ADCON5Lbits.C1RDY == 0);
    ADCON3Hbits.C1EN = 1;

    //Turn on and configure shared core
    ADCON5Lbits.SHRPWR = 1;
    // Wait when the shared core is ready for operation
    while(ADCON5Lbits.SHRRDY == 0);
    // Turn on digital power to enable triggers to the shared core
    ADCON3Hbits.SHREN = 1;
}