function entityParser(text: string): string {
    return text
        .replace(/&gt;/g, `>`)
        .replace(/&lt;/g, `<`)
        .replace(/&frasl;/g, `/`)
        .replace(/&quot;/g, `"`)
        .replace(/&apos;/g, `'`)
        .replace(/&amp;/g, `&`)
};