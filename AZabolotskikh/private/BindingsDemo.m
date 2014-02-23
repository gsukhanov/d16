//
//  BindingsDemo.m
//  ZJVM
//
//  Created by zaxdo on 23.02.14.
//  Copyright (c) 2014 zaxdo. All rights reserved.
//

#import <Cocoa/Cocoa.h>


@interface SimpleClass : NSObject {
	int value;
}
@property (assign)int value;
@end

@implementation SimpleClass
@synthesize value;
@end

int main(int argc, const char **argv)
{
	SimpleClass *this = [[SimpleClass alloc] init];
	SimpleClass *that = [[SimpleClass alloc] init];
	[this setValue:8];
	[that setValue:6];
	printf("%d, %d", [this value], [that value]); //Prints "8, 6"
	[that bind:@"value" toObject:this withKeyPath:@"value" options:nil];
	printf("%d, %d", [this value], [that value]); //Prints "6, 6"
	[that setValue:42];
	printf("%d, %d", [this value], [that value]); //Prints "42, 42"
	return 0;

}