/*--- Day 2: Cube Conundrum ---

You're launched high into the atmosphere! The apex of your trajectory just barely reaches the surface of a large island floating in the sky. You gently land in a fluffy pile of leaves. It's quite cold, but you don't see much snow. An Elf runs over to greet you.

The Elf explains that you've arrived at Snow Island and apologizes for the lack of snow. He'll be happy to explain the situation, but it's a bit of a walk, so you have some time. They don't get many visitors up here; would you like to play a game in the meantime?

As you walk, the Elf shows you a small bag and some cubes which are either red, green, or blue. Each time you play this game, he will hide a secret number of cubes of each color in the bag, and your goal is to figure out information about the number of cubes.

To get information, once a bag has been loaded with cubes, the Elf will reach into the bag, grab a handful of random cubes, show them to you, and then put them back in the bag. He'll do this a few times per game.

You play several games and record the information from each game (your puzzle input). Each game is listed with its ID number (like the 11 in Game 11: ...) followed by a semicolon-separated list of subsets of cubes that were revealed from the bag (like 3 red, 5 green, 4 blue).

For example, the record of a few games might look like this:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

In game 1, three sets of cubes are revealed from the bag (and then put back again). The first set is 3 blue cubes and 4 red cubes; the second set is 1 red cube, 2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.

The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with that configuration. However, game 3 would have been impossible because at one point the Elf showed you 20 red cubes at once; similarly, game 4 would also have been impossible because the Elf showed you 15 blue cubes at once. If you add up the IDs of the games that would have been possible, you get 8.

Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?
*/

#include "stdbool.h"
#include "stdio.h"
#include "stdlib.h"
#include "string.h" // strstr to find substring ; strtok could also be useful

// c data structures
// arrays in stack, arrays in heap
// struct
// enum?

//       V              V                       V
// Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
//
//       V                V                       V
// Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
//
//       V                        V                        V
// Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
//
//       V                       V               V
// Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
//
//       V                       V
// Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

struct cubeset { int quantity; const char *desc; };

static const size_t GAMESET_LEN = 3;
static const struct cubeset GAMESET[] = {
	{ .quantity = 12, .desc = "red" },
	{ .quantity = 13, .desc = "green" },
	{ .quantity = 14, .desc = "blue" },
};

bool cube_desc_valid(const char *desc, struct cubeset *gameset, size_t nsets)
{
	for (int i = 0; i < nsets; i++) {
		if (strcmp(desc, gameset[i].desc) == 0)
			return true;
	}
	return false;
}

bool game_is_valid(const char *game, struct cubeset *gameset, size_t nsets)
{
	// game is only valid if it contains at least one cube with a .desc from gameset
	// game is only valid...
	return false;
}
/*
int parse_game(const char *line, int *game_id, struct cubeset *moves, size_t nmoves)
{
	// for each substring from index 1 (i.e. after "Game:")
	// Find location after "Game:"
	
	const char *cur = strtok(line, 'Game ');
	long score = 0;

	while (game != NULL) {
		if (!game_is_valid(line, GAMESET, GAMESET_LEN))
			

		game = strtok(NULL, ';');
	}
}
*/
long score_game_p1(const char *line, size_t len)
{

	return 1;
}

long solve_first_problem(const char *game_info_path)
{
	char *line = NULL;
	size_t line_len = 0;
	long total_score = 0;
	FILE *game_info_file = fopen(game_info_path, "r");
	
	// TODO: Read line by line
	while (getline(&line, &line_len, game_info_file) != -1) {
		total_score += score_game_p1(line, line_len);
		free(line);
		line = NULL;
	}
	
	// TODO: close file
	fclose(game_info_file);

	// return solution
	return total_score;
}

void print_gamestr(const char *gamestr, int gamestr_len)
{
	for (int i = 0; i < gamestr_len; i++) {
		if (gamestr[i] == '\0')
			printf("NULL");

		printf("%c", gamestr[i]);
	}
}

int main(int argc, char **argv)
{
	char *game_info_path = "input.txt";
	long solution1, solution2;

	if (argc > 1) {
		game_info_path = argv[1];
	}

	const char *teststr_ = "Game 1: 1 a, 4 b; 5 c, 1 a";

	char *teststr = strdup(teststr_);

	printf("starting state: teststr: ");
	print_gamestr(teststr, strlen(teststr_));
	printf("\n");

	char *token = strtok(teststr, ":");
	printf("delim: ':', token: '%s', teststr: ", token);
	print_gamestr(teststr, strlen(teststr_));
	printf("\n");

	token = strtok(NULL, ";");
	printf("delim: ';', token: '%s', teststr: ", token);
	print_gamestr(teststr, strlen(teststr_));
	printf("\n");

	token = strtok(NULL, ";");
	printf("delim: ';', token: '%s', teststr: ", token);
	print_gamestr(teststr, strlen(teststr_));
	printf("\n");

	token = strtok(NULL, ";");
	printf("delim: ';', token: '%s', teststr: ", token);
	print_gamestr(teststr, strlen(teststr_));
	printf("\n");

	printf("path: %s\n", game_info_path);

	//solution1 = solve_first_problem(game_info_path);
	//printf("solution1: %ld\n", solution1);

	return 0;
}
