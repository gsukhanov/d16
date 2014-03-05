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
	private int packFlags()
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
	private void unpackFlags(int packed) {
		fC = ((packed & 0x1) > 0);
		fZ = ((packed & 0x2) > 0);
		fID = ((packed & 0x4) > 0);
		fD = ((packed & 0x8) > 0);
		boolean newM = (packed & 0x20) > 0;
		fO = ((packed & 0x40) > 0);
		fN = ((packed & 0x80) > 0);

		if (fE) {
			fX = fM = false;
		} else {
			fX = ((packed & 0x10) > 0);
			if (this.fX)
			{ 
				rX &= 255;
				rY &= 255;
			}
			if (newM != fM) {
				if (newM) {
					rB = (rA >> 8); rA &= 255;
				} else {
					rA |= rB << 8;
				}
				fM = newM;
			}
		}
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
		return fM ? 128 : 32768;
	}
	private int negativeMaskX() {
		return fX ? 128 : 32768;
	}
	private int overflowMaskM() {
		return fM ? 255 : 65535;
	}
	private int popByte() {
		int ret = readByte(rSP);
		if (fE)
			rSP = (rSP + 1 & 0xFF | rSP & 0xFF00);
		else {
			rSP = (rSP + 1 & 0xFFFF);
		}
		return ret;
	}
	private int popByteR() {
		int ret = readByte(rR);
		rR = (rR + 1 & 0xFFFF);
		return ret;
	}
	private int popWordR() {
		int ret = popByteR();
		ret |= (popByteR() << 8);
		return ret;
	}
	//This is for all of the instructions
	private void instruction_brk() {
		pushWord(rPC);
		pushByte(packFlags());
		fBRK = true;
		rPC = brkVector;
	}
	private void instruction_or(int input) {
		rA |= input;
		fZ = rA == 0;
		fN = (rA & negativeMaskM()) > 0;
	}
	private void instruction_and(int input) {
		rA &= input;
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
		pushByte(packFlags());
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
	private void instruction_jsr(int addr)
	{
		pushWord(rPC + 1);
		rPC = addr;
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
	private void instruction_ent() {
		pushWordR(rI);
		rI = (rPC + 2);
		rPC = readShort(rPC);
	}
	private void instruction_bit(int input) {
		fO = ((input & (fM ? 0x40 : 0x4000) ) > 0);
		fN = ((input & (fM ? 0x80 : 0x8000)) > 0);
		fZ = ((input & rA) > 0);
	}
	private void instruction_bit() {
		fZ = ((readWord() & rA) == 0);
	}
	private void instruction_rol(int input) {
		int i = readWord(input);
		int n = (i << 1 | (fC ? 1 : 0)) & overflowMaskM();
		fC = ((i & negativeMaskM()) > 0);
		fN = ((n & negativeMaskM()) > 0);
		fZ = (n == 0);
		writeLocation(input, n);
	}
	private void instruction_rol() {
		int n = (rA << 1 | (fC ? 1 : 0)) & overflowMaskM();
		fC = ((rA & negativeMaskM()) > 0);
		rA = n;
		fN = ((rA & negativeMaskM()) > 0);
		fZ = (rA == 0);
	}
	private void instruction_plp() {
		unpackFlags(popByte());
	}
	private void instruction_rli() {
		rI = popWordR();
		fN = ((rI & negativeMaskX()) > 0);
		fZ = (rI == 0);
	}
	private void instruction_bmi() {
		if (fN) {
			branch();
		}
	}
	private void instruction_sec() {
		fC = true;
	}
	private void instruction_dec() {
		rA = (rA - 1 & overflowMaskM());
		fN = ((rA & negativeMaskM()) > 0);
		fZ = (rA == 0);
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
			break;
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
			instruction_jsr(getAbsoluteAddress());
			break;
		case 0xFC:
			instruction_jsr(readShort(getAbsoluteIndexedXAddress()));
			break;
		case 0x21:
			instruction_and(readWord(getIndexedIndirectAddress()));
			break;
		case 0x23:
			instruction_and(readWord(getStackRelativeAddress()));
			break;
		case 0x25:
			instruction_and(readWord(getZeroPageAddress()));
			break;
		case 0x27:
			instruction_and(readWord(getRStackRelativeAddress()));
			break;
		case 0x29:
			instruction_and(readWord());
			break;
		case 0x2D:
			instruction_and(readWord(getAbsoluteAddress()));
			break;
		case 0x31:
			instruction_and(readWord(getIndirectIndexedAddress()));
			break;
		case 0x32:
			instruction_and(readWord(getIndirectAddress()));
			break;
		case 0x33:
			instruction_and(readWord(getStackRealativeIndirectIndexedAddress()));
			break;
		case 0x35:
			instruction_and(readWord(getZeroPageXAddress()));
			break;
		case 0x37:
			instruction_and(readWord(getRStackRealativeIndirectIndexedAddress()));
			break;
		case 0x39:
			instruction_and(readWord(getAbsoluteIndexedYAddress()));
			break;
		case 0x3D:
			instruction_and(readWord(getAbsoluteIndexedXAddress()));
			break;
		case 0x22:
			instruction_ent();
			break;
		case 0x24:
			instruction_bit(readWord(getZeroPageAddress()));
			break;
		case 0x2C:
			instruction_bit(readWord(getAbsoluteAddress()));
			break;
		case 0x34:
			instruction_bit(readWord(getZeroPageXAddress()));
			break;
		case 0x3C:
			instruction_bit(readWord(getAbsoluteIndexedXAddress()));
			break;
		case 0x89:
			instruction_bit();
			break;
		case 0x26:
			instruction_rol(getZeroPageAddress());
			break;
		case 0x2A:
			instruction_rol();
			break;
		case 0x2E:
			instruction_rol(getAbsoluteAddress());
			break;
		case 0x36:
			instruction_rol(getZeroPageXAddress());
			break;
		case 0x3E:
			instruction_rol(getAbsoluteIndexedXAddress());
			break;
		case 0x28:
			instruction_plp();
			break;
		case 0x2B:
			instruction_rli();
			break;
		case 0x30:
			instruction_bmi();
			break;
		case 0x38:
			instruction_sec();
			break;
		case 0x3A:
			instruction_dec();
			break;
		}
	}
}
