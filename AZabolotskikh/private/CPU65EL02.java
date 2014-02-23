package to.zaxdo.cpuemu;

public class CPU65EL02 {
	private byte[] memory;
	private int rSP;
	private int rPC;
	private int rA;
	private int rB;
	private int rX;
	private int rY;
	private int rR;
	private int rI;
	private int rD;
	private boolean fC;
	private boolean fZ;
	private boolean fID;
	private boolean fD;
	private boolean fBRK;
	private boolean fO;
	private boolean fN;
	private boolean fE;
	private boolean fM;
	private boolean fX;
	private boolean busMapped;
	private int busAt;
	private int memoryExtensions;
	private int brkVector;

	public CPU65EL02() {
		memory = new byte[65536];
		rPC = 0;
		busMapped = false;
	}
	private void mIncPC()
	{
		rPC++;
		rPC &= 0xFFFF;
	}
	private int readByte(int loc) {
		loc &= 0xFFFF;
		if (busMapped && loc >= busAt && loc <= busAt + 256) {
			//TODO: process bus
		}
		int memoryExtensionsNeeded = loc >> 13;
		if (memoryExtensionsNeeded > memoryExtensions) {
			return 0xFF;
		}
		return memory[loc];
	}
	private void branch() {
		int offset = readByte(rPC); mIncPC();
		rPC = rPC + offset & 0xFFFF;
	}
	private int readWord(int loc){
		int i = readByte(loc);
		if (!fM)
		{
			i |= readByte(loc + 1) << 8;
		}
		return i;
	}
	private int readWord(){
		int i = readWord(rPC);
		mIncPC();
		if (!fM) {
			mIncPC();
		}
		return i;
	}
	private int readShort(int loc) {
		//this is the same as readWord, but it always reads 16 bits, regardless of M flag
		int i = readByte(loc);
		i |= readByte(loc + 1) << 8;
		return i;
	}
	private void pushByte(int data) {
		if (fE)
			rSP = (rSP - 1 & 0xFF | rSP & 0xFF00);
		else {
			rSP = (rSP - 1 & 0xFFFF);
		}
		writeLocation(rSP, data);
	}
	private void pushByteR(int data) {
		rR = (rR - 1 & 0xFFFF);
		writeLocation(rR, data);
	}
	private void writeLocation(int loc, int data) {
		//TODO: do something
	}
	private void pushWord(int data)
	{
		pushByte(data >> 8);
		pushByte(data & 0xFF);
	}
	private void pushWordR(int data)
	{
		pushByteR(data >> 8);
		pushByteR(data & 0xFF);
	}
	private int flagsToInt()
	{
		int result = fN ? 1 : 0;
		result <<= 1;
		result += fO ? 1 : 0;
		result <<= 1;
		result += fM ? 1 : 0;
		result <<= 1;
		result += fX ? 1 : 0;
		result <<= 1;
		result += fD ? 1 : 0;
		result <<= 1;
		result += fID ? 1 : 0;
		result <<= 1;
		result += fZ ? 1 : 0;
		result <<= 1;
		result += fC ? 1 : 0;
		return result;
	}

	//This is for all of 65el02 addressing modes
	private int getAbsoluteIndexedYAddress() {
		int i = readByte(rPC); mIncPC();
		i |= readByte(rPC) << 8; mIncPC();
		return i + rY & 0xFFFF;
	}
	private int getAbsoluteIndexedXAddress() {
		int i = readByte(rPC); mIncPC();
		i |= readByte(rPC) << 8; mIncPC();
		return i + rX & 0xFFFF;
	}
	private int getIndexedIndirectAddress()
	{
		int i = readByte(rPC) + rX & 0xFF;mIncPC();
		int j = readByte(i);
		j |= readByte(i + 1) << 8;
		return j;
	}
	private int getZeroPageAddress() {
		int i = readByte(rPC) & 0xFF;
		mIncPC();
		return i;
	}
	private int getZeroPageXAddress() {
		int i = readByte(rPC) + rX;mIncPC();
		if (fX) {
			i &= 0xFF;
		}
		return i;
	}
	private int getStackRelativeAddress() {
		int i = readByte(rPC) + rSP & 0xFFFF; mIncPC();
		return i;
	}
	private int getRStackRelativeAddress() {
		int i = readByte(rPC) + rR & 0xFFFF; mIncPC();
		return i;
	}
	private int getAbsoluteAddress() {
		int i = readByte(rPC); mIncPC();
		i |= readByte(rPC) << 8; mIncPC();
		return i;
	}
	private int getStackRealativeIndirectIndexedAddress() {
		int i = readByte(rPC) + rSP & 0xFFFF; mIncPC();
		return readShort(i) + rY & 0xFFFF;
	}
	private int getRStackRealativeIndirectIndexedAddress() {
		int i = readByte(rPC) + rR & 0xFFFF; mIncPC();
		return readShort(i) + rY & 0xFFFF;
	}
	private int getIndirectIndexedAddress() {
		int i = readByte(rPC); mIncPC();
		int j = readByte(i);
		j |= readByte(i + 1) << 8;
		return j + rY & 0xFFFF;
	}
	private int getIndirectAddress() {
		int i = readByte(rPC);mIncPC();
		int j = readByte(i);
		j |= readByte(i + 1) << 8;
		return j;
	}

	private int negativeMaskM() {
		return fM ? 1<<7 : 1<<15; 
	} 
	private int overflowMaskM() {
		return fM ? (1<<8)-1 : (1<<16)-1; 
	}
	//This is for all of the instructions
	private void instruction_brk() {
		pushWord(rPC);
		pushByte(flagsToInt());
		fBRK = true;
		rPC = brkVector;
	}
	private void instruction_or(int input) {
		rA |= input;
		fZ = rA == 0;
		fN = (rA & negativeMaskM()) > 0;
	}
	private void instruction_nxt() {
		rPC = readWord(rI);
		rI += 2;
	}
	private void instruction_tsb(int input) {
		fZ = (input & rA) > 0;
		rA |= input;
	}
	private void instruction_trb(int input) {
		fZ = (input & rA) > 0;
		rA |= (input ^ 0xFFFFFFFF);
	}
	private void instruction_asl() {
		fC = (rA & negativeMaskM()) > 0;
		rA = rA << 1 & overflowMaskM();
		fZ = rA == 0;
		fN = (rA & negativeMaskM()) > 0;
	}
	private void instruction_asl(int input) {
		int i = readWord(input);
		fC = (i & negativeMaskM()) > 0;
		i = i << 1 & overflowMaskM();
		fZ = i == 0;
		fN = (i & negativeMaskM()) > 0;
		writeLocation(input, i);
	}
	private void instruction_php() {
		pushByte(flagsToInt());
	}
	private void instruction_rhi() {
		pushWordR(rI);
	}
	private void instruction_bpl() {
		if (!fN) branch();
	}
	private void instruction_inc() {
		rA = rA + 1 & negativeMaskM();
		fZ = rA == 0;
		fN = (rA & negativeMaskM()) > 0;
	}
	private void instruction_inc(int input) {
		int i = readWord(input);
		rA = i + 1 & negativeMaskM();
		fZ = i == 0;
		fN = (i & negativeMaskM()) > 0;
		writeLocation(input, i);
	}
	private void instruction_rhx()
	{
		if (this.fX) 
			pushByteR(rX);
		else
			pushWordR(rX);
	}
	private void instruction_jsr()
	{
		pushWord(rPC + 1);
		rPC = getAbsoluteAddress();
	}
	private void instruction_mul(int input) {
		long i;
		if (fM)
		{
			if (fC)
				i = (byte)input * (byte)rA;
			else {
				i = input * rA;
			}
			rA = (int)(i & 0xFF);
			rD = (int)(i >> 8 & 0xFF);
		}
		else
		{
			if (fC)
				i = (short)input * (short)rA;
			else {
				i = input * rA;
			}
			rA = (int)(i & 0xFFFF);
			rD = (int)(i >> 16 & 0xFFFF);
		}
		fO = (rD != 0) && (rD != (fC ? 65535 : 255));
		fN = (i < 0);
		fZ = (i == 0);
	}
	private void instruction_clc() {
		fC = false;
	}
	private void processInstruction() {
		int instruction = readByte(rPC);
		mIncPC();
		switch (instruction) {
		case 0x0:
			instruction_brk();
			break;
		case 0x1:
			instruction_or(readWord(getIndexedIndirectAddress()));
			break;
		case 0x3:
			instruction_or(readWord(getStackRelativeAddress()));
			break;
		case 0x5:
			instruction_or(readWord(getZeroPageAddress()));
			break;
		case 0x7:
			instruction_or(readWord(getRStackRelativeAddress()));
			break;
		case 0x9:
			instruction_or(readWord());
			break;
		case 0xD:
			instruction_or(readWord(getAbsoluteAddress()));
			break;
		case 0x11:
			instruction_or(readWord(getIndirectIndexedAddress()));
			break;
		case 0x12:
			instruction_or(readWord(getIndirectAddress()));
			break;
		case 0x13:
			instruction_or(readWord(getStackRealativeIndirectIndexedAddress()));
			break;
		case 0x15:
			instruction_or(readWord(getZeroPageXAddress()));
			break;
		case 0x17:
			instruction_or(readWord(getRStackRealativeIndirectIndexedAddress()));
			break;
		case 0x19:
			instruction_or(readWord(getAbsoluteIndexedYAddress()));
			break;
		case 0x1D:
			instruction_or(readWord(getAbsoluteIndexedXAddress()));
			break;
		case 0x2:
			instruction_nxt();
			break;
		case 0x4:
			instruction_tsb(readWord(getZeroPageAddress()));
			break;
		case 0xC:
			instruction_tsb(readWord(getAbsoluteAddress()));
			break;
		case 0x6:
			instruction_asl(getZeroPageAddress());
			break;
		case 0xA:
			instruction_asl();
			break;
		case 0xE:
			instruction_asl(getAbsoluteAddress());
			break;
		case 0x16:
			instruction_asl(getZeroPageXAddress());
			break;
		case 0x1E:
			instruction_asl(getAbsoluteIndexedXAddress());
			break;
		case 0x8:
			instruction_php();
			break;
		case 0xB:
			instruction_rhi();
			break;
		case 0xF:
			instruction_mul(readWord(getZeroPageAddress()));
			break;
		case 0x1F:
			instruction_mul(readWord(getZeroPageXAddress()));
			break;
		case 0x2F:
			instruction_mul(readWord(getAbsoluteAddress()));
			break;
		case 0x3F:
			instruction_mul(readWord(getAbsoluteIndexedXAddress()));
			break;
		case 0x10:
			instruction_bpl();
			break;
		case 0x18:
			instruction_clc();
			break;
		case 0x1A:
			instruction_inc();
			break;
		case 0xE6:
			instruction_inc(getZeroPageAddress());
			break;
		case 0xEE:
			instruction_inc(getAbsoluteAddress());
			break;
		case 0xFE:
			instruction_inc(getAbsoluteIndexedXAddress());
		case 0xF6:
			instruction_inc(getZeroPageXAddress());
			break;
		case 0x14:
			instruction_trb(readWord(getZeroPageAddress()));
			break;
		case 0x1C:
			instruction_trb(readWord(getAbsoluteAddress()));
			break;
		case 0x1B:
			instruction_rhx();
			break;
		case 0x20:
			instruction_jsr();
			break;
			
		default:
			break;
		}
	}
}
