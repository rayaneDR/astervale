// SPDX-License-Identifier: Apache-2.0
import java.io.*;
import java.nio.charset.StandardCharsets;
import java.nio.file.*;
import java.util.*;
import org.astervale.panel.IntentEngine;
public final class Benchmark {
    public static void main(String[] args)throws Exception{
        if(args.length>2)System.setOut(new java.io.PrintStream(args[2],java.nio.charset.StandardCharsets.UTF_8));
        IntentEngine engine=new IntentEngine(Files.newBufferedReader(Path.of(args[0]),StandardCharsets.UTF_8));
        Map<String,int[]> scores=new LinkedHashMap<>();List<String> errors=new ArrayList<>();
        List<String> rows=Files.readAllLines(Path.of(args[1]),StandardCharsets.UTF_8);
        long start=System.nanoTime();
        for(String row:rows.subList(1,rows.size())){String[] p=row.split("\t",3);IntentEngine.Result r=engine.parse(p[1],p[0]);int[] score=scores.computeIfAbsent(p[0],k->new int[2]);score[1]++;if(r.action().name().equals(p[2]))score[0]++;else errors.add("| "+p[0]+" | "+p[1]+" | "+p[2]+" | "+r.action()+" |");}
        System.out.println("# Text-route benchmark\n\nExecuted on Windows JVM, not A51. Synthetic human-authored fixtures, no recorded speech; curated keyword matcher, no LLM. Does not establish general language quality, speech WER, phone latency, RAM or battery.\n");
        System.out.println("| Language | Correct / cases | A51 speech / TTS / LLM |\n| --- | --- | --- |");
        scores.forEach((lang,s)->System.out.println("| "+lang+" | "+s[0]+" / "+s[1]+" | untested |"));
        System.out.println("\n## Failures\n\n| Language | Input | Expected | Actual |\n| --- | --- | --- | --- |");errors.forEach(System.out::println);
        System.out.println("\nNegation, quoted text, inflected words and code-switching require broader tests. Tool execution always needs confirmation, including matched routes.\n");
        System.out.println("Host batch elapsed (not device latency): "+((System.nanoTime()-start)/1_000_000)+" ms");
    }
}
